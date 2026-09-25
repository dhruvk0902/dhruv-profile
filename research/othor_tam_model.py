"""
Othor AI market-sizing model: TAM, SAM, SOM (India + US, companies with 50+ employees).
Prepared September 2026. All values are annual software subscription value in USD, 2026.

Every input is tagged:
  [S] sourced fact (source listed in the report, section 14)
  [A] assumption (ranked in the report, section 12)
  [C] calculated from [S] and [A]

Run:  python3 othor_tam_model.py
Change any [A] input below and rerun to see the effect on every output.
"""
import math

BANDS = ["50-199", "200-999", "1,000-4,999", "5,000+"]

# ---------------------------------------------------------------------------
# 1. ACV table [A], supplied by Othor AI, not yet confirmed with the founder
# ---------------------------------------------------------------------------
ACV = {
    "low":  [2_400, 7_000, 15_000, 60_000],
    "base": [4_800, 11_000, 37_500, 155_000],
    "high": [7_200, 15_000, 60_000, 250_000],
}
FULL_ROLLOUT_ACV_5000 = 1_000_000   # founder's internal estimate, separate scenario only
NON_CONSUMER_ACV_FACTOR = 0.50      # [A] non-consumers pay 50% of band ACV

# ---------------------------------------------------------------------------
# 2. US universe: SUSB-anchored firm-size (Zipf / Pareto) model
# ---------------------------------------------------------------------------
US_FIRMS_500_PLUS_2022 = 21_041          # [S] SBA Advocacy FAQ 2026, from SUSB 2022
US_FIRMS_500_PLUS_2007 = 18_469          # [S] Census SUSB 2007
US_FIRMS_5000_PLUS_2007 = 1_956          # [S] Census SUSB 2007
US_FIRMS_5000_PLUS_2019 = 2_230          # [S] SUSB 2019 via Certified EO (cross-check only)
US_FIRMS_10_PLUS_2019 = 1_311_698        # [S] SUSB 2019 via Certified EO (cross-check only)
AXTELL_ALPHA = 1.06                      # [S] Axtell (2001), Science: US firm sizes follow Zipf, alpha ~1.06


def us_counts(alpha_low=AXTELL_ALPHA, n500=US_FIRMS_500_PLUS_2022):
    ratio_5000_500 = US_FIRMS_5000_PLUS_2007 / US_FIRMS_500_PLUS_2007   # [C] 0.106
    alpha_tail = -math.log10(ratio_5000_500)                             # [C] 0.975
    n = {
        50: n500 * (500 / 50) ** alpha_low,
        200: n500 * (500 / 200) ** alpha_low,
        1000: n500 * (500 / 1000) ** alpha_tail,
        5000: n500 * ratio_5000_500,
    }
    bands = [n[50] - n[200], n[200] - n[1000], n[1000] - n[5000], n[5000]]
    return bands, alpha_tail, n


# ---------------------------------------------------------------------------
# 3. India universe: EPFO-anchored Pareto model
# ---------------------------------------------------------------------------
EPFO_ESTABLISHMENTS_FY24 = 766_000       # [S] EPFO Annual Report 2023-24 (contributing establishments)
EPFO_MEMBERS_FY24 = 73_700_000           # [S] EPFO Annual Report 2023-24 (contributing members)
EPFO_THRESHOLD = 20                      # [S] EPF Act applies to establishments with 20+ employees
SHARE_BELOW_20 = 0.25                    # [A] share of EPFO establishments with <20 members
MEAN_BELOW_20 = 10                       # [A] mean members in those establishments
ESTAB_TO_COMPANY = 0.80                  # [A] companies per EPFO establishment code


def india_counts(f=SHARE_BELOW_20, c=ESTAB_TO_COMPANY, small_mean=MEAN_BELOW_20):
    n20 = (1 - f) * EPFO_ESTABLISHMENTS_FY24
    mean20 = (EPFO_MEMBERS_FY24 - f * EPFO_ESTABLISHMENTS_FY24 * small_mean) / n20
    alpha = mean20 / (mean20 - EPFO_THRESHOLD)       # Pareto mean = xmin * a / (a - 1)

    def N(s):
        return n20 * (EPFO_THRESHOLD / s) ** alpha

    est = [N(50) - N(200), N(200) - N(1000), N(1000) - N(5000), N(5000)]
    return [x * c for x in est], alpha, est, N


# ---------------------------------------------------------------------------
# 4. BI adoption by size: Eurostat 2023 log-linear curve
# ---------------------------------------------------------------------------
EU_ANALYTICS_SMALL = 23.6    # [S] Eurostat 2023: small (10-49) enterprises, data analytics by own employees
EU_ANALYTICS_LARGE = 68.6    # [S] Eurostat 2023: large (250+)
REP_SIZE_SMALL = 16.4        # [C] median firm size of the 10-49 class under Zipf
REP_SIZE_LARGE = 500         # [C] median firm size of the 250+ class under Zipf
REP_SIZE_BANDS = [79, 326, 1_676, 10_180]   # [C] median firm size of each band (US Zipf model)
EU_CAP = 95                  # [A] ceiling on adoption
US_UPLIFT_PP = 8             # [A] US ahead of EU average by 8 points
INDIA_GAP_PP = 12            # [A] India behind EU average by 12 points


def eu_curve():
    slope = (EU_ANALYTICS_LARGE - EU_ANALYTICS_SMALL) / math.log(REP_SIZE_LARGE / REP_SIZE_SMALL)
    return [min(EU_CAP, EU_ANALYTICS_SMALL + slope * math.log(m / REP_SIZE_SMALL)) for m in REP_SIZE_BANDS], slope


def bi_rates(us_uplift=US_UPLIFT_PP, india_gap=INDIA_GAP_PP):
    eu, _ = eu_curve()
    us = [min(97, r + us_uplift) / 100 for r in eu]
    ind = [max(0, min(97, r - india_gap)) / 100 for r in eu]
    return {"US": us, "India": ind}


# Digital-systems filter: share of BI non-consumers that run operations on ERP,
# CRM, accounting software (e.g. Tally) or databases [A]
DIGITAL = {"US": [0.85, 0.92, 0.97, 0.97], "India": [0.75, 0.85, 0.95, 0.95]}


# ---------------------------------------------------------------------------
# 5. TAM
# ---------------------------------------------------------------------------
def tam(counts, acv, bi, digital=DIGITAL, nc_factor=NON_CONSUMER_ACV_FACTOR, acv_5000_override=None,
        india_acv_factor=1.0):
    rows, tot = [], {"gross": 0, "L1": 0, "L2": 0, "users": 0, "digital_non": 0, "non_digital": 0}
    for country in ("US", "India"):
        for i, band in enumerate(BANDS):
            n = counts[country][i]
            a = acv[i]
            if acv_5000_override and i == 3:
                a = acv_5000_override
            if country == "India":
                a *= india_acv_factor
            users = n * bi[country][i]
            non = n - users
            dig_non = non * digital[country][i]
            gross = n * a
            l1 = users * a
            l2 = dig_non * nc_factor * a
            rows.append((country, band, n, a, users, dig_non, non - dig_non, gross, l1, l2))
            tot["gross"] += gross
            tot["L1"] += l1
            tot["L2"] += l2
            tot["users"] += users
            tot["digital_non"] += dig_non
            tot["non_digital"] += non - dig_non
    tot["TAM"] = tot["L1"] + tot["L2"]
    return rows, tot


# ---------------------------------------------------------------------------
# 6. SAM: priority verticals, one primary vertical per company
# ---------------------------------------------------------------------------
# US manufacturing, from SUSB 2022 via NAM
US_MFG_FIRMS = 239_265          # [S]
US_MFG_500_PLUS = 4_177         # [S]
US_MFG_SHARE_UNDER_100 = 0.931  # [S]
US_MFG_DEDUPE = [0.95, 0.85, 0.70, 0.60]   # [A] keep only firms whose primary sector is manufacturing

# Shares of the non-manufacturing remainder in each band [A]
US_SHARE = {"FS": 0.08, "DL": 0.12, "REC": 0.09, "MS_POOL": 0.30}
US_MULTI = [0.45, 0.75, 0.95, 1.00]     # [A] share of retail/food/health firms with 2+ establishments

# India
INDIA_MFG_SHARE = [0.45, 0.45, 0.40, 0.35]  # [A] informed by AQEES (38.5% of workers) and ASI (1 in 5 factories 100+);
                                            # lower at the top because IT/BPO and GCCs dominate 1,000+ in India
INDIA_FS_COUNTS = [0, 954, 300, 80]     # [C/A] 63 insurers + 671 NBFC-UL/ML [S] + ~300 base-layer NBFCs + ~300 banks/AMCs/brokers [A]
INDIA_SHARE = {"DL": 0.12, "REC": 0.08, "MS_POOL": 0.25}
INDIA_MULTI = [0.35, 0.65, 0.90, 1.00]  # [A]


def us_mfg_bands():
    n100 = US_MFG_FIRMS * (1 - US_MFG_SHARE_UNDER_100)
    alpha_m = math.log(n100 / US_MFG_500_PLUS) / math.log(5)
    _, alpha_tail, _ = us_counts()
    n50 = n100 * 2 ** alpha_m
    n200 = US_MFG_500_PLUS * 2.5 ** alpha_m
    n1000 = US_MFG_500_PLUS * 0.5 ** alpha_tail
    n5000 = US_MFG_500_PLUS * 10 ** (-alpha_tail)
    raw = [n50 - n200, n200 - n1000, n1000 - n5000, n5000]
    return [r * d for r, d in zip(raw, US_MFG_DEDUPE)], raw, alpha_m, n100


def sam_counts(counts, us_share=US_SHARE, us_multi=US_MULTI, india_mfg=INDIA_MFG_SHARE,
               india_share=INDIA_SHARE, india_multi=INDIA_MULTI):
    out = {}
    mfg, _, _, _ = us_mfg_bands()
    us = []
    for i in range(4):
        n = counts["US"][i]
        m = min(mfg[i], n)
        r = n - m
        big = i >= 1
        fs = r * us_share["FS"] if big else 0
        dl = r * us_share["DL"] if big else 0
        rec = r * us_share["REC"] if big else 0
        ms = r * us_share["MS_POOL"] * us_multi[i]
        us.append({"Manufacturing": m, "Insurance and financial services": fs,
                   "Distribution and logistics": dl, "Real estate and construction": rec,
                   "Multi-site operators": ms})
    out["US"] = us
    ind = []
    for i in range(4):
        n = counts["India"][i]
        m = n * india_mfg[i]
        fs = min(INDIA_FS_COUNTS[i], n - m)
        r = n - m - fs
        big = i >= 1
        dl = r * india_share["DL"] if big else 0
        rec = r * india_share["REC"] if big else 0
        ms = r * india_share["MS_POOL"] * india_multi[i]
        ind.append({"Manufacturing": m, "Insurance and financial services": fs,
                    "Distribution and logistics": dl, "Real estate and construction": rec,
                    "Multi-site operators": ms})
    out["India"] = ind
    return out


def value_per_company(acv, bi, digital=DIGITAL, nc=NON_CONSUMER_ACV_FACTOR):
    """Expected annual value per company in each band (both layers)."""
    return {c: [bi[c][i] * acv[i] + (1 - bi[c][i]) * digital[c][i] * nc * acv[i] for i in range(4)]
            for c in ("US", "India")}


def sam_value(sc, acv, bi, **kw):
    v = value_per_company(acv, bi, **kw)
    total, n_total = 0, 0
    by_vertical = {}
    for c in ("US", "India"):
        for i in range(4):
            for vert, n in sc[c][i].items():
                total += n * v[c][i]
                n_total += n
                by_vertical.setdefault((c, vert), [0, 0])
                by_vertical[(c, vert)][0] += n
                by_vertical[(c, vert)][1] += n * v[c][i]
    return total, n_total, by_vertical


# ---------------------------------------------------------------------------
# 7. SOM: sales-capacity build [A] (not a revenue forecast)
# ---------------------------------------------------------------------------
YEARS = [2027, 2028, 2029, 2030, 2031]
AES = [4, 8, 12, 12, 12]           # [A] quota-carrying salespeople; flat from 2029
NEW_AE_PRODUCTIVITY = 0.5          # [A] first-year salesperson at 50%
DEALS_PER_AE = 15                  # [A] new logos per ramped salesperson per year
FOUNDER_DEALS = 6                  # [A] founder-led new logos per year
LOGO_CHURN = 0.15                  # [A] annual logo churn
AE_MIX = [0.30, 0.45, 0.20, 0.05]  # [A] share of salesperson deals by band
FOUNDER_MIX = [0, 0, 0.5, 0.5]     # [A] founder-led deals are enterprise


def som(acv, bi, aes=AES, deals=DEALS_PER_AE, founder=FOUNDER_DEALS, churn=LOGO_CHURN):
    # expected ACV of a closed deal in each band: users pay full ACV, digital non-consumers 50%
    exp_acv = []
    for i in range(4):
        vals = []
        for c in ("US", "India"):
            b, d = bi[c][i], DIGITAL[c][i]
            addressable = b + (1 - b) * d
            vals.append((b * acv[i] + (1 - b) * d * NON_CONSUMER_ACV_FACTOR * acv[i]) / addressable)
        exp_acv.append(sum(vals) / 2)            # [A] 50/50 India-US deal split
    active = [0.0] * 4
    history = []
    prev_aes = 0
    for y, n_ae in zip(YEARS, aes):
        new_hires = max(0, n_ae - prev_aes)
        effective = (n_ae - new_hires) + new_hires * NEW_AE_PRODUCTIVITY
        prev_aes = n_ae
        ae_deals = effective * deals
        new = [ae_deals * AE_MIX[i] + founder * FOUNDER_MIX[i] for i in range(4)]
        active = [a * (1 - churn) + nw for a, nw in zip(active, new)]
        value = sum(a * e for a, e in zip(active, exp_acv))
        history.append((y, n_ae, effective, ae_deals + founder, sum(active), value, list(active)))
    return history, exp_acv


# ---------------------------------------------------------------------------
# 8. Top-down cross-check
# ---------------------------------------------------------------------------
INDIA_SOFTWARE_2026 = 24.7e9       # [S] Gartner, Nov 2025
WORLD_SOFTWARE_2026 = 1.4e12       # [S] Gartner, Feb 2026 (">$1.4 trillion")
US_SHARE_OF_NA = 0.90              # [A]
SHARE_SPEND_50_PLUS = 0.90         # [A] share of BI spend from companies with 50+ employees
FBI_SOFTWARE_SHARE = 0.75          # [A] Fortune figure includes services


def top_down():
    india_share = INDIA_SOFTWARE_2026 / WORLD_SOFTWARE_2026
    out = {}
    # Fortune Business Insights: BI market (software + services), 2026 = $37.96B, North America 31% (2025)
    g = 37.96e9
    out["Fortune Business Insights"] = g * (0.31 * US_SHARE_OF_NA + india_share) * FBI_SOFTWARE_SHARE * SHARE_SPEND_50_PLUS
    # Grand View Research: BI software, 2025 = $40.1B, to $81.45B by 2033; North America 37% (2025)
    cagr = (81.45 / 40.1) ** (1 / 8) - 1
    g2 = 40.1e9 * (1 + cagr)
    out["Grand View Research"] = g2 * (0.37 * US_SHARE_OF_NA + india_share) * SHARE_SPEND_50_PLUS
    return out, india_share, cagr


# ---------------------------------------------------------------------------
# Reporting helpers
# ---------------------------------------------------------------------------
def fm(x):
    if abs(x) >= 1e9:
        return f"${x / 1e9:.2f}B"
    if abs(x) >= 1e6:
        return f"${x / 1e6:.0f}M"
    if abs(x) >= 1e3:
        return f"${x / 1e3:.0f}k"
    return f"${x:.0f}"


def fn(x):
    return f"{x:,.0f}"


def main():
    us, alpha_tail, us_n = us_counts()
    ind, alpha_in, ind_est, ind_N = india_counts()
    counts = {"US": us, "India": ind}
    bi = bi_rates()
    eu, slope = eu_curve()

    print("## Universe")
    print(f"US alpha_tail={alpha_tail:.3f}; US N>=50={fn(us_n[50])} N>=200={fn(us_n[200])} "
          f"N>=1000={fn(us_n[1000])} N>=5000={fn(us_n[5000])}")
    print(f"Cross-check alpha from SUSB 2019 N>=10 and 2022 N>=500: "
          f"{math.log(US_FIRMS_10_PLUS_2019 / US_FIRMS_500_PLUS_2022) / math.log(50):.3f}")
    print(f"India alpha={alpha_in:.3f}; establishments by band={[fn(x) for x in ind_est]}")
    print(f"India N>=100 est={fn(ind_N(100))}; N>=500 est={fn(ind_N(500))}; "
          f"N>=10 (extrapolated)={fn(ind_N(10))}; share 500+ of 10+={ind_N(500) / ind_N(10):.3%}")
    for c in ("US", "India"):
        print(c, [fn(x) for x in counts[c]], "total", fn(sum(counts[c])))

    print("\n## BI adoption")
    print(f"EU slope={slope:.2f} pp per ln-unit; EU curve={[round(x, 1) for x in eu]}")
    for c in ("US", "India"):
        print(c, [f"{x:.0%}" for x in bi[c]])

    print("\n## TAM by band (base ACV)")
    for scen in ("low", "base", "high"):
        rows, t = tam(counts, ACV[scen], bi)
        print(f"{scen}: gross={fm(t['gross'])} L1={fm(t['L1'])} L2={fm(t['L2'])} TAM={fm(t['TAM'])} "
              f"L2 share={t['L2'] / t['TAM']:.0%}")
        if scen == "base":
            for r in rows:
                c, b, n, a, users, dn, nd, gross, l1, l2 = r
                print(f"  {c:5} {b:12} n={fn(n):>8} acv={fm(a):>6} users={fn(users):>8} dig_non={fn(dn):>8} "
                      f"non_dig={fn(nd):>7} gross={fm(gross):>8} L1={fm(l1):>8} L2={fm(l2):>8}")
            print(f"  users={fn(t['users'])} digital_non={fn(t['digital_non'])} non_digital={fn(t['non_digital'])}")
    _, t_full = tam(counts, ACV["base"], bi, acv_5000_override=FULL_ROLLOUT_ACV_5000)
    print(f"Full-rollout scenario (5,000+ at $1M): TAM={fm(t_full['TAM'])}")

    print("\n## SAM")
    mfg, raw, alpha_m, n100 = us_mfg_bands()
    print(f"US mfg alpha={alpha_m:.3f} n100={fn(n100)} raw={[fn(x) for x in raw]} deduped={[fn(x) for x in mfg]}")
    sc = sam_counts(counts)
    for c in ("US", "India"):
        for i, b in enumerate(BANDS):
            print(c, b, {k: fn(v) for k, v in sc[c][i].items()}, "sum", fn(sum(sc[c][i].values())),
                  f"share of band {sum(sc[c][i].values()) / counts[c][i]:.0%}")
    for scen in ("low", "base", "high"):
        total, n_total, byv = sam_value(sc, ACV[scen], bi)
        print(f"SAM {scen}: {fm(total)} companies={fn(n_total)}")
        if scen == "base":
            for k, (n, v) in sorted(byv.items()):
                print(f"  {k[0]:5} {k[1]:34} n={fn(n):>8} value={fm(v)}")
    v = value_per_company(ACV["base"], bi)
    print("value per company base", {c: [fm(x) for x in v[c]] for c in v})

    print("\n## SOM")
    sam_base = sam_value(sc, ACV["base"], bi)[0]
    for scen in ("low", "base", "high"):
        hist, exp_acv = som(ACV[scen], bi)
        sam_s = sam_value(sc, ACV[scen], bi)[0]
        print(f"{scen}: expected ACV per deal={[fm(x) for x in exp_acv]}")
        for y, n_ae, eff, new, act, val, act_b in hist:
            print(f"  {y} AEs={n_ae} effective={eff} new logos={new:.0f} active={act:.0f} value={fm(val)} "
                  f"share of SAM={val / sam_s:.2%} by band={[round(x) for x in act_b]}")

    print("\n## Top-down")
    td, india_share, cagr = top_down()
    _, tb = tam(counts, ACV["base"], bi)
    print(f"India share of world software={india_share:.2%}; Grand View implied CAGR={cagr:.1%}")
    for k, val in td.items():
        print(f"  {k}: {fm(val)}  ratio to bottom-up TAM={val / tb['TAM']:.1f}x ; to L1={val / tb['L1']:.1f}x")
    users = tb["users"]
    print(f"  BI-using companies={fn(users)}; implied avg BI software spend per user company: "
          + ", ".join(f"{k}={fm(val / users)}" for k, val in td.items()))
    wavg = tb["L1"] / users
    print(f"  Othor AI base ACV weighted over BI users={fm(wavg)}")

    print("\n## Sensitivity on base TAM")
    base = tb["TAM"]
    tests = {}
    tests["ACV table low/high"] = (tam(counts, ACV["low"], bi)[1]["TAM"], tam(counts, ACV["high"], bi)[1]["TAM"])
    for a in (1.0, 1.1):
        pass
    us_lo, _, _ = us_counts(alpha_low=1.0)
    us_hi, _, _ = us_counts(alpha_low=1.1)
    tests["US count slope (alpha 1.0/1.1)"] = (tam({"US": us_lo, "India": ind}, ACV["base"], bi)[1]["TAM"],
                                              tam({"US": us_hi, "India": ind}, ACV["base"], bi)[1]["TAM"])
    in_lo = india_counts(f=0.40, c=0.65)[0]
    in_hi = india_counts(f=0.10, c=0.95)[0]
    tests["India counts (EPFO small share 40%/10%, company factor 0.65/0.95)"] = (
        tam({"US": us, "India": in_lo}, ACV["base"], bi)[1]["TAM"],
        tam({"US": us, "India": in_hi}, ACV["base"], bi)[1]["TAM"])
    tests["BI adoption (US +0/+15pp, India -20/-5pp)"] = (
        tam(counts, ACV["base"], bi_rates(0, 20))[1]["TAM"], tam(counts, ACV["base"], bi_rates(15, 5))[1]["TAM"])
    tests["Non-consumer ACV factor (30%/70%)"] = (
        tam(counts, ACV["base"], bi, nc_factor=0.3)[1]["TAM"], tam(counts, ACV["base"], bi, nc_factor=0.7)[1]["TAM"])
    dlo = {c: [max(0, x - 0.10) for x in DIGITAL[c]] for c in DIGITAL}
    dhi = {c: [min(1, x + 0.10) for x in DIGITAL[c]] for c in DIGITAL}
    tests["Digital filter (-10pp/+10pp)"] = (tam(counts, ACV["base"], bi, digital=dlo)[1]["TAM"],
                                            tam(counts, ACV["base"], bi, digital=dhi)[1]["TAM"])
    tests["India ACV at 50% of table / 100%"] = (tam(counts, ACV["base"], bi, india_acv_factor=0.5)[1]["TAM"], base)
    tests["5,000+ band ACV $60k / $250k (others base)"] = (
        tam(counts, ACV["base"][:3] + [60_000], bi)[1]["TAM"], tam(counts, ACV["base"][:3] + [250_000], bi)[1]["TAM"])
    for k, (lo, hi) in sorted(tests.items(), key=lambda kv: -(abs(kv[1][1] - kv[1][0]))):
        print(f"  {k:70} low={fm(lo):>8} high={fm(hi):>8} swing={fm(hi - lo):>8} "
              f"({(lo - base) / base:+.0%} / {(hi - base) / base:+.0%})")

    print("\n## SOM sensitivity (year 5, base ACV)")
    y5 = som(ACV["base"], bi)[0][-1][5]
    for label, kw in [("deals per AE 10/20", ({"deals": 10}, {"deals": 20})),
                      ("AEs flat 8 / 20 from 2029", ({"aes": [4, 8, 8, 8, 8]}, {"aes": [4, 8, 20, 20, 20]})),
                      ("churn 25%/8%", ({"churn": 0.25}, {"churn": 0.08})),
                      ("founder deals 3/12", ({"founder": 3}, {"founder": 12}))]:
        lo = som(ACV["base"], bi, **kw[0])[0][-1][5]
        hi = som(ACV["base"], bi, **kw[1])[0][-1][5]
        print(f"  {label:30} low={fm(lo)} high={fm(hi)} base={fm(y5)}")

    print("\n## 2035 sanity check")
    _, exp_acv = som(ACV["base"], bi)
    blended = sum(m * e for m, e in zip(AE_MIX, exp_acv))
    ent = (exp_acv[2] + exp_acv[3]) / 2
    sc_total = sam_value(sc, ACV["base"], bi)[1]
    for target in (50e6, 75e6):
        for label, a in (("salesperson mix", blended), ("mid-market only (200-999)", exp_acv[1]),
                         ("enterprise mix (1,000+)", ent)):
            cust = target / a
            print(f"  {fm(target)} at {label} ACV {fm(a)}: {fn(cust)} customers = {cust / sc_total:.2%} of SAM "
                  f"companies; = {target / sam_base:.1%} of base SAM value")


if __name__ == "__main__":
    main()
