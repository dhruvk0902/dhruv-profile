# Othor AI: TAM, SAM and SOM (India and US, 2026)

Market-sizing evidence base. Prepared September 2026. Audience: the founder, for internal planning and for reuse with investors.

All market values are annual software subscription value in US dollars, 2026. Services and implementation are excluded.

## How to read this report

- **[S]** sourced fact. The number after S points to the source list in section 14 (for example [S1]).
- **[A]** assumption. The number after A points to the ranked assumption register in section 12 (for example [A3]).
- **[C]** calculated from sourced facts and assumptions. Every calculation is shown in section 11.
- Company counts are rounded to three significant figures. Dollar values are rounded to one decimal place in billions or millions. Totals may not add exactly because of rounding.
- The full model is in `othor_tam_model.py` next to this file. Change any [A] input and rerun it to see the effect on every output.

### Data-access note (read this first)

The research environment's network allowlist blocked direct access to census.gov, bls.gov, sba.gov, rbi.org.in, mospi.gov.in, epfindia.gov.in and ec.europa.eu. Figures from those sources were read from search-engine extracts of the pages, not from the files themselves. Section 14 marks every source "search extract, verify". One gap matters most. The US counts by detailed size band come from a firm-size model anchored on sourced totals, not from the SUSB 2022 detailed-size table itself. Replacing the modelled counts with that table takes one person about 30 minutes, and it is the first item on the verification list (section 12).

### Confirmations used

| Item | Status |
|---|---|
| Audience | Both investors and internal planning |
| ACV table | Used exactly as supplied. **Not yet confirmed with the founder** [A1] |
| Sales capacity for SOM | Not supplied. Assumed and flagged [A14 to A20]. SOM rests on these assumptions |

---

## 1. Summary

| Measure | Low | Base | High | Definition |
|---|---|---|---|---|
| **TAM** | $1.2B | **$2.5B** | $3.7B | Annual value if every company with 50+ employees in India and the US that already uses BI, or runs on digital systems without BI, bought Othor AI at its band ACV |
| of which Layer 1: displacement and coexistence | $1.0B | $2.0B | $3.0B | Companies already using BI or an in-house analytics function |
| of which Layer 2: non-consumption | $0.3B | $0.5B | $0.7B | Companies on ERP, CRM, accounting software or databases with no BI, at 50% of band ACV |
| **SAM** | $0.6B | **$1.3B** | $1.9B | The part of TAM in Othor AI's current verticals and size filters, in India and the US |
| **SOM, year 3 (2029)** | $2.7M | **$6.2M** | $9.7M | Annual contract value of the customers an assumed sales team could win and keep by 2029 |
| **SOM, year 5 (2031)** | $5.3M | **$11.9M** | $18.6M | The same, by 2031 |
| Full-rollout scenario TAM (separate, founder estimate) | $3.8B | $4.8B | $5.8B | TAM with the 5,000+ band at $1M ACV per company. Never used in the base case |

Low, base and high use the low, base and high ACV columns. Company counts and adoption rates are held at base. Section 8 shows how the other assumptions move the answer.

**Key facts behind the numbers** [C]:

- Universe: 396,000 companies with 50+ employees. The US has 242,000 and India has 154,000.
- 196,000 of them (49%) already use BI or run in-house analytics. That is the displacement and coexistence layer.
- 163,000 (41%) run on digital systems but have no BI. That is the non-consumption layer. 85% of them have 50 to 199 employees.
- 37,000 (9%) have neither BI nor the digital systems to feed it. They are excluded.
- SOM ≤ SAM ≤ TAM holds in every case. Year 5 base SOM is 0.95% of base SAM, and base SAM is 51% of base TAM.

**Three things the founder should know:**

1. **Price sets the TAM, not company count.** The ACV table moves TAM by ±50%. No count or adoption assumption moves it by more than ±11%.
2. **The bottom-up TAM is conservative against the money already spent.** Published BI market estimates, scaled to India and the US, put today's BI software spend at $7.6B to $13.8B. That is 3.1x to 5.6x the bottom-up TAM. The gap comes from price. Companies that use BI spend an implied $39k to $71k a year on it, against Othor AI's weighted base ACV of $10k.
3. **Non-consumption is real but mid-market heavy.** It adds 163,000 companies and $0.5B. Most of that value sits in 50 to 199 employee firms, where traditional BI does not work without a data team.

---

## 2. Universe: companies with 50+ employees, by size band

### 2.1 Counts used

| Band (employees) | US companies (2022) | India companies (FY2023-24) | Total |
|---|---|---|---|
| 50-199 | 186,000 [C] | 125,000 [C] | 311,000 |
| 200-999 | 44,900 [C] | 25,300 [C] | 70,100 |
| 1,000-4,999 | 8,480 [C] | 3,720 [C] | 12,200 |
| 5,000+ | 2,230 [C] | 642 [C] | 2,870 |
| **Total** | **242,000** | **154,000** | **396,000** |

### 2.2 US method: SUSB totals plus a firm-size curve

The SUSB 2022 detailed-size table could not be opened (see the data-access note). The counts are modelled from sourced SUSB totals using the best-documented regularity in firm-size data. US firm sizes follow a Zipf (power-law) distribution, so the number of firms at or above size *s* falls in proportion to *s* raised to the power *−α*.

| Input | Value | Tag |
|---|---|---|
| Firms with 500+ employees, 2022 | 21,041 | [S1] |
| Employer firms, 2022 | 6.4 million | [S1] |
| Firms with 500+ and 5,000+ employees, 2007 | 18,469 and 1,956 | [S2] |
| Zipf exponent for US firms | about 1.06 | [S4] |
| Tail exponent above 500 employees, from the 2007 ratio (1,956 / 18,469 = 0.106) | 0.975 | [C] |

**Cross-checks that the curve fits:**

- The model gives 2,230 firms with 5,000+ employees. A secondary source quoting SUSB 2019 gives 1,108 + 582 + 540 = 2,230 [S3]. They match.
- SUSB 2019 has 1,311,698 firms with 10+ employees [S3]. Fitting that and the 2022 count of 500+ firms implies an exponent of 1.056 [C]. Axtell's published 1.06 [S4] agrees.

**Scope notes:**

- SUSB covers employer firms. It excludes public administration, farms and private households. It includes nonprofits such as hospitals and universities.
- A firm is counted by total US employment across all its establishments.

### 2.3 India method and data quality

India has no official count of companies by employee band. MCA does not record employees. Udyam classifies by turnover and investment. Every available proxy is shown below.

| Proxy | What it counts | Latest figure | Band split available? | Use in this report |
|---|---|---|---|---|
| **EPFO** | Establishments registered for provident fund. Mandatory at 20+ employees [S9] | 766,000 contributing establishments and 73.7 million contributing members, FY2023-24 [S8] | No public band split found. Mean is 96 members per establishment [C] | **Chosen as the base.** It covers every sector and is employee-based |
| AQEES / QES (Labour Bureau) | Establishments with 10+ workers in 9 sectors | 1.4% have 500+ workers; about 80% have 10 to 99 (January to March 2022) [S10] | Coarse bands | Cross-check on the upper tail |
| ASI (MoSPI) | Registered factories | 260,061 factories (2023-24) [S11]; one in five has 100+ workers (2023) [S12] | In the full tables, which could not be retrieved | Manufacturing cross-check and SAM input |
| Udyam (MSME Ministry) | Enterprises classified by investment and turnover | 37,042 medium enterprises out of about 47.2 million registrations (snapshot date not stated) [S13] | Turnover only | Cross-check for the middle bands |
| GST (GSTN) | Tax registrations by turnover | Not used | Turnover. One company holds many registrations | Not used |
| MCA, CMIE Prowess | Registered or listed companies | Not retrieved (MCA has no employee field; Prowess is paid) | No or partial | Not used |

**How the EPFO count becomes size bands** (full arithmetic in section 11.2):

1. Assume 25% of EPFO establishments have fewer than 20 members, averaging 10 each [A4]. These are voluntary registrations and firms that shrank below the threshold.
2. Fit a Pareto curve to the rest. Its mean of 125 members implies an exponent of 1.19 [C]. That is steeper than the US 1.06, which matches the well-known "missing middle" in Indian firm sizes.
3. Read establishment counts at 50, 200, 1,000 and 5,000 members off the curve [C].
4. Convert establishments to companies at 0.8 companies per establishment code [A4]. Some companies hold several codes, for example one per state or unit.

**Cross-checks:**

- **Upper tail.** The model puts 0.95% of 10+ establishments at 500+ [C]. AQEES says 1.4% [S10]. They agree within 1.5x.
- **Mid-market.** The model gives 63,300 companies with 100 to 999 employees [C]. Udyam's 37,042 registered medium enterprises (about ₹50 crore to ₹250 crore turnover under the old definition) should sit inside that range, and they do [S13].
- **Manufacturing.** ASI implies about 52,000 factories with 100+ workers [C]. The model gives 84,600 establishments with 100+ members across all sectors [C]. On those figures, factories would be 62% of the 100+ tier, well above manufacturing's 38.5% of AQEES workers [S10]. One reason: ASI counts contract workers in a factory's headcount, while EPFO registers contract workers under their contractor. That makes factories look larger in ASI than their EPFO registration.

**Quality verdict: weak.**

- The tested range for the India counts is -33% to +39% in the 50-199 band and -25% to +22% in the 1,000-4,999 band. The top of the curve is well pinned by the EPFO mean. The bottom depends on the <20 share [A4].
- That range is tested in section 8. It moves TAM by ±9%.

### 2.4 Known limitations

- **Multinationals are counted in both countries.** India has 2,117 Global Capability Centres with 2.36 million staff, run by, among others, 506 Forbes Global 2000 companies [S31]. Many of their US parents are in the US 5,000+ band. If about 1,000 GCCs sit in India's 1,000+ bands [A], the overlap is roughly $0.05B to $0.1B, or 2% to 4% of TAM [C]. GCC analytics purchasing is usually decided at headquarters.
- **Different base years.** US counts are 2022 and India counts are FY2023-24. Neither is grown to 2026. That keeps both slightly conservative.
- **US bands are modelled.** They are not read from the SUSB detailed-size table. Replace them when that table is available.

---

## 3. Bottom-up TAM

TAM = sum over bands of (companies using BI x band ACV) + (digital non-consumers x 50% of band ACV). Section 4 derives the split. The "gross" column is the plain count x ACV ceiling.

| Country | Band | Companies [C] | Base ACV [A1] | Gross ceiling [C] | Layer 1 value [C] | Layer 2 value [C] | **TAM, base [C]** | Count source |
|---|---|---|---|---|---|---|---|---|
| US | 50-199 | 186,000 | $4,800 | $893M | $467M | $181M | **$648M** | [S1][S2][S4] |
| US | 200-999 | 44,900 | $11,000 | $494M | $350M | $66M | **$416M** | [S1][S2][S4] |
| US | 1,000-4,999 | 8,480 | $37,500 | $318M | $294M | $12M | **$306M** | [S1][S2] |
| US | 5,000+ | 2,230 | $155,000 | $345M | $335M | $5M | **$340M** | [S1][S2][S3] |
| **US total** | | **242,000** | | **$2.1B** | **$1.4B** | **$0.3B** | **$1.7B** | |
| India | 50-199 | 125,000 | $4,800 | $599M | $193M | $152M | **$345M** | [S8][S9] |
| India | 200-999 | 25,300 | $11,000 | $278M | $142M | $58M | **$200M** | [S8][S9] |
| India | 1,000-4,999 | 3,720 | $37,500 | $139M | $101M | $18M | **$119M** | [S8][S9] |
| India | 5,000+ | 642 | $155,000 | $99M | $83M | $8M | **$91M** | [S8][S9] |
| **India total** | | **154,000** | | **$1.1B** | **$0.5B** | **$0.2B** | **$0.8B** | |
| **Total** | | **396,000** | | **$3.2B** | **$2.0B** | **$0.5B** | **$2.5B** | |

**Low and high cases** [C]:

| Case | Gross ceiling | Layer 1 | Layer 2 | TAM |
|---|---|---|---|---|
| Low ACV | $1.6B | $1.0B | $0.3B | $1.2B |
| Base ACV | $3.2B | $2.0B | $0.5B | $2.5B |
| High ACV | $4.7B | $3.0B | $0.7B | $3.7B |

**Full-rollout scenario (founder's internal estimate, shown separately).** The founder estimates a 5,000-employee enterprise could reach about $1M a year at full company-wide rollout. On-premise deployments push deals toward $100k and above. Pricing the 5,000+ band at $1M and holding everything else at base lifts TAM from $2.5B to $4.8B [C]. The low case goes to $3.8B and the high case to $5.8B. This is an upside scenario only. It is never used in the base case.

**Pricing note [A3].** The ACV table applies the same USD prices in India and the US. If Indian deals close at half the US price, base TAM falls from $2.5B to $2.1B.

---

## 4. Non-consumption layer

### 4.1 The two filters

**Filter 1: does the company already use BI?** No US or India survey of BI adoption by employee band was found. The proxy is Eurostat's 2023 measure of enterprises whose own employees perform data analytics [S16]. That fits the definition needed here, "has BI or an analyst function", closely.

| Eurostat 2023 anchor | Share | Tag |
|---|---|---|
| Small enterprises (10 to 49 employees) | 23.6% | [S16] |
| Large enterprises (250+) | 68.6% | [S16] |
| All enterprises with 10+ | 28.2% | [S16] |

Adoption rises with the log of company size. A straight line through the two anchors adds 13.2 percentage points each time company size multiplies by e (about 2.7x) [C]. Reading the line at each band's median company size gives the EU rate. The US rate adds 8 points [A6]. The India rate subtracts 12 points [A6].

| Band | Median company size [C] | EU rate [C] | **US rate** [C] | **India rate** [C] |
|---|---|---|---|---|
| 50-199 | 79 | 44% | **52%** | **32%** |
| 200-999 | 326 | 63% | **71%** | **51%** |
| 1,000-4,999 | 1,680 | 85% | **93%** | **73%** |
| 5,000+ | 10,200 | 95% (capped) [A26] | **97%** (capped) | **83%** |

- India-specific BI adoption by size: **not found**.
- The only India proxy found is a 2025 CMR study: 67% of Indian MSMEs are "digitally equipped" and 43% show competence in ERP and cloud [S18]. It is not by size band and not about BI. That is why India is set 12 points below the EU curve rather than derived.

**Filter 2: does a non-consumer run on digital systems?** A company counts as a digital non-consumer only if it runs operations on ERP, CRM, accounting software such as Tally, or databases.

| Band | US [A8] | India [A8] | Evidence |
|---|---|---|---|
| 50-199 | 85% | 75% | EU ERP use: 37.9% of small firms to 86.3% of large (2023) [S17]. "Digital systems" is broader than ERP because it includes accounting software |
| 200-999 | 92% | 85% | EU CRM use: 22% of small firms to 61% of large [S17] |
| 1,000+ | 97% | 95% | India: GST e-invoicing has been mandatory above ₹5 crore annual turnover since 1 August 2023 [S19] |

The India e-invoicing threshold is about $0.52M at ₹95.80 per USD [S26]. A 50-employee Indian firm crosses it at about ₹10 lakh (about $10,400) of revenue per employee. So almost every company in the India universe must already issue machine-readable e-invoices. That is why the India digital filter is set high despite lower BI maturity.

### 4.2 Result per band (base)

| Country | Band | Companies | Using BI (Layer 1) | Digital non-consumers (Layer 2) | Non-digital, excluded | Layer 2 value at 50% ACV [A5] |
|---|---|---|---|---|---|---|
| US | 50-199 | 186,000 | 97,300 | 75,400 | 13,300 | $181M |
| US | 200-999 | 44,900 | 31,800 | 12,000 | 1,040 | $66M |
| US | 1,000-4,999 | 8,480 | 7,840 | 614 | 19 | $12M |
| US | 5,000+ | 2,230 | 2,160 | 65 | 2 | $5M |
| India | 50-199 | 125,000 | 40,300 | 63,300 | 21,100 | $152M |
| India | 200-999 | 25,300 | 12,900 | 10,500 | 1,860 | $58M |
| India | 1,000-4,999 | 3,720 | 2,700 | 971 | 51 | $18M |
| India | 5,000+ | 642 | 533 | 104 | 5 | $8M |
| **Total** | | **396,000** | **196,000** | **163,000** | **37,400** | **$500M** |

### 4.3 What this means

- **41% of the universe is non-consumption** [C]. That is 163,000 companies that run on digital systems and have no BI.
- They are worth $0.5B at half-price ACV, which is 20% of base TAM. Base Layer 1 is $2.0B.
- 85% of these companies have 50 to 199 employees. That is exactly the segment where BI tools stall, because they assume a data team and defined KPIs.
- **In India, the 50-199 band is majority non-consumption.** 68% of those 125,000 companies have no BI. Three-quarters of those run on digital systems [C].
- **Why this is a real market, not a theoretical one.** These companies already produce structured data (e-invoices, ERP and accounting ledgers). What they lack is the analyst layer. Othor AI's automatic metric discovery supplies that layer. No existing BI market report counts these companies, because they have no BI line item.
- **Why the value share is modest.** The layer is smaller in value than in count because non-consumers cluster in the cheapest band and are priced at 50% of ACV [A5]. If non-consumers paid 70% of band ACV, TAM would rise by 8%.

---

## 5. Top-down cross-check

Market reports use different definitions. Each estimate is scaled on its own and none are combined.

### 5.1 Estimates found

| Publisher | Definition | Figure | Year | Tag |
|---|---|---|---|---|
| Fortune Business Insights | Business intelligence market. The report segments into platforms and services; the software share is assumed at 75% [A24] | $34.82B (2025); $37.96B (2026); $72.21B (2034); CAGR 8.4%; North America 31.0% of 2025 | 2026 edition | [S20] |
| Grand View Research | Business intelligence **software** market | $40.1B (2025); $81.45B (2033), an implied CAGR of 9.3% [C]; North America 37% of 2025 | 2026 to 2033 report | [S21] |
| Gartner | "Analytic platforms" software (a segment of Gartner's data and analytics software market) | $41.92B in 2024, up 17.3%. The whole data and analytics software market was $175.17B, up 13.9% | 2024 | [S22] |
| Mordor Intelligence, Polaris, Precedence, The Business Research Company | BI market (various definitions) | $37.73B, $35.30B, $47.04B and $85.65B (2025) | 2025 | [S23] |

Most global BI estimates for 2025 cluster between $35B and $47B. The Business Research Company's $85.65B clearly uses a broader definition and is set aside. Gartner's 2024 analytic platforms figure ($41.92B) is already above most publishers' 2025 BI figures, which fits a broader definition. Gartner publishes no regional split for it, so it is not scaled.

### 5.2 Scaling to India plus US, 2026, companies with 50+ employees

| Step | Fortune Business Insights | Grand View Research |
|---|---|---|
| Global 2026 | $37.96B [S20] | $40.1B x 1.093 = $43.8B [C] |
| US share = North America share x 90% [A21] | 31% x 90% = 27.9% | 37% x 90% = 33.3% |
| India share = India software spend / world software spend, 2026: $24.7B / $1.4T [S24][S25] | 1.76% [C] | 1.76% [C] |
| India plus US value | $11.3B | $15.4B |
| Software only (x 75%) [A24] | $8.4B | not needed (software only) |
| Companies with 50+ employees (x 90%) [A23] | **$7.6B** | **$13.8B** |

### 5.3 Comparison and why the gap exceeds 2x

| | Value | Ratio to bottom-up TAM ($2.5B) | Ratio to bottom-up Layer 1 ($2.0B) |
|---|---|---|---|
| Fortune Business Insights, scaled | $7.6B | 3.1x | 3.9x |
| Grand View Research, scaled | $13.8B | 5.6x | 7.0x |

The top-down figures are 3.1x to 5.6x the bottom-up TAM. Three reasons, in order of size:

1. **Price, not company count.**
   - Dividing scaled BI spend by the 196,000 companies that use BI gives an implied average of $39k to $71k per company a year [C].
   - Othor AI's base ACV averaged over the same companies is $10k [C].
   - The company counts agree. The price per company does not.
   - This means the bottom-up TAM prices Othor AI's replacement of existing spend at a fraction of today's wallet. It is conservative on purpose.
2. **Concentration at the top.**
   - Large enterprises run multi-product BI and analytics stacks. Othor AI's $155,000 base ACV for 5,000+ companies is well below what those stacks cost.
   - The founder's full-rollout scenario ($1M in the 5,000+ band) lifts TAM to $4.8B. That narrows the gap to the Fortune figure to 1.6x.
3. **Scope.** Top-down figures include government, education and other buyers outside SUSB. They also include adjacent spend, such as embedded analytics and reporting tools, that Othor AI would not replace.

**Conclusion.**

- Layer 1 of the bottom-up TAM ($2.0B) sits inside an existing BI wallet of $7.6B to $13.8B in India and the US. Othor AI would take share of that wallet at a lower price per company.
- Layer 2 ($0.5B) is not in any top-down figure at all.

---

## 6. SAM

### 6.1 Definitions and the no-double-counting rule

Each company is assigned to exactly one **primary** vertical. That is the sector holding most of its employees.

| Vertical | US scope | India scope | Size filter |
|---|---|---|---|
| Manufacturing | NAICS 31-33 | Manufacturing (ASI and AQEES coverage) | 50+ |
| Insurance and financial services | NAICS 52 | IRDAI insurers, RBI-registered NBFCs, banks, AMCs, brokers | 200+ |
| Distribution and logistics | NAICS 42 plus 48-49 (including warehousing networks) | Wholesale trade, transport and storage | 200+ |
| Real estate and construction | NAICS 23 plus 53 | Construction and real estate | 200+ |
| Multi-site operators | Retail (44-45), food services (722) and health care (62, excluding social assistance), **with two or more establishments** | Retail chains, restaurant chains and cloud kitchens, hospital, diagnostic and clinic chains, with two or more sites | 50+ |

How double counting is prevented:

1. **US manufacturing** counts come from SUSB via NAM [S6]. SUSB counts a firm in every sector where it has an establishment. So dedupe factors of 0.95, 0.85, 0.70 and 0.60 by band [A12] keep only firms whose primary sector is manufacturing.
2. **India insurance and financial services** counts come from regulator lists, which are unique legal entities. They are removed before the rest is allocated.
3. **All other verticals** are fixed shares of the non-manufacturing (and in India, non-financial) remainder of each band. The shares sum to under 100%, so no company can land in two verticals, and every SAM company is inside the TAM universe.
4. **Warehousing networks** go to distribution and logistics, not to multi-site operators.

### 6.2 Inputs

| Input | US | India | Tag |
|---|---|---|---|
| Manufacturing | 239,265 firms; 4,177 with 500+; 93.1% under 100 (2022) | 45%, 45%, 40% and 35% of each band. Lower at the top because IT/BPO and GCCs dominate India's 1,000+ bands | US [S6]; India [A11], informed by [S10][S11][S12] |
| Insurance and financial services | 8% of the non-manufacturing remainder, 200+ bands | 1,334 companies. Built from 63 insurers with material staff and 671 upper- and middle-layer NBFCs, plus about 300 base-layer NBFCs and 300 banks, AMCs and brokers [A13]. Split 954 / 300 / 80 across the 200-999, 1,000-4,999 and 5,000+ bands | US [A9]; India 74 insurers [S14] and 15 upper-layer plus 656 middle-layer NBFCs out of about 9,000 [S15] |
| Distribution and logistics | 12% of remainder | 12% of remainder | [A9]. India informed by AQEES: trade plus transport are 9.9% of workers [S10] |
| Real estate and construction | 9% of remainder | 8% of remainder | [A9] |
| Multi-site pool (retail, food, health) | 30% of remainder | 25% of remainder. Health alone is 10.6% of AQEES workers [S10] | [A9] |
| Share of multi-site pool with 2+ establishments, by band | 45%, 75%, 95%, 100% | 35%, 65%, 90%, 100% | [A10]. Anchor: only about 294,000 US firms are multi-location, but they own 2.3 million establishments [S7] |

**Note on insurers.** IRDAI lists 74 insurers: 26 life, 25 general, 8 standalone health, 2 specialised and 13 reinsurers [S14]. Eleven of the 13 reinsurers are assumed to be foreign reinsurer branches with small Indian staff, leaving 63 [A13].

### 6.3 SAM company counts (base)

| Country | Band | Manufacturing | Insurance and FS | Distribution and logistics | Real estate and construction | Multi-site operators | **SAM companies** | Share of band |
|---|---|---|---|---|---|---|---|---|
| US | 50-199 | 19,700 | excluded | excluded | excluded | 22,500 | **42,100** | 23% |
| US | 200-999 | 5,960 | 3,110 | 4,670 | 3,500 | 8,760 | **26,000** | 58% |
| US | 1,000-4,999 | 1,180 | 584 | 876 | 657 | 2,080 | **5,370** | 63% |
| US | 5,000+ | 265 | 157 | 236 | 177 | 589 | **1,420** | 64% |
| India | 50-199 | 56,100 | excluded | excluded | excluded | 6,000 | **62,100** | 50% |
| India | 200-999 | 11,400 | 954 | 1,550 | 1,040 | 2,100 | **17,000** | 67% |
| India | 1,000-4,999 | 1,490 | 300 | 232 | 155 | 435 | **2,610** | 70% |
| India | 5,000+ | 225 | 80 | 40 | 27 | 84 | **456** | 71% |
| **Total** | | **96,300** | **5,190** | **7,610** | **5,550** | **42,500** | **157,000** | 40% |

### 6.4 SAM value

SAM value per company uses the same two-layer logic as TAM: users pay full ACV, and digital non-consumers pay 50%.

| Country | Band | SAM companies | Value per company, base [C] | **SAM value, base** [C] |
|---|---|---|---|---|
| US | 50-199 | 42,100 | $3,480 | $147M |
| US | 200-999 | 26,000 | $9,280 | $241M |
| US | 1,000-4,999 | 5,370 | $36,100 | $194M |
| US | 5,000+ | 1,420 | $153,000 | $217M |
| India | 50-199 | 62,100 | $2,770 | $172M |
| India | 200-999 | 17,000 | $7,900 | $134M |
| India | 1,000-4,999 | 2,610 | $32,100 | $84M |
| India | 5,000+ | 456 | $141,000 | $64M |
| **Total** | | **157,000** | | **$1.3B** |

| By vertical | US companies | US value | India companies | India value | **Total value** |
|---|---|---|---|---|---|
| Manufacturing | 27,100 | $207M | 69,200 | $325M | **$532M** |
| Multi-site operators | 33,900 | $324M | 8,630 | $59M | **$383M** |
| Distribution and logistics | 5,780 | $111M | 1,830 | $25M | **$136M** |
| Real estate and construction | 4,340 | $83M | 1,220 | $17M | **$100M** |
| Insurance and financial services | 3,850 | $74M | 1,330 | $28M | **$102M** |
| **Total** | **74,900** | **$799M** | **82,200** | **$455M** | **$1.3B** |

**SAM by case** [C]: low $0.6B, base $1.3B, high $1.9B. SAM is 50% to 51% of TAM in every case.

**Reading the SAM:**

- Manufacturing is the largest vertical by value ($0.5B) and by count (96,300 companies). Most of it is in India.
- Insurance and financial services is small in count but high in value per logo. Upper- and middle-layer NBFCs and insurers sit mostly in the top bands.

---

## 7. SOM: sales-capacity build

SOM is derived from assumed go-to-market capacity, not picked as a share of SAM. **It is a ceiling on what the assumed team could reach. It is not a forecast of Othor AI's revenue.** No sales-capacity figures were supplied, so every input below is an assumption to confirm.

### 7.1 Inputs

| Input | Value | Tag |
|---|---|---|
| Quota-carrying salespeople | 2027: 4; 2028: 8; 2029 onward: 12 | [A14] |
| First-year productivity | 50% | [A20] |
| New customers per ramped salesperson per year | 15 | [A15] |
| Founder-led deals per year | 6, all in the 1,000+ bands | [A16] |
| Annual customer churn | 15% | [A17] |
| Salesperson deal mix by band | 30% / 45% / 20% / 5% | [A18] |
| Country split of deals | 50% India, 50% US | [A19] |
| Expected ACV of a won deal, base, by band [C] | $3,540 / $9,010 / $34,300 / $148,000 | Band ACV, weighted by users at full ACV and non-consumers at 50% |

**Calibration.** 15 deals at the blended salesperson deal value of $19,400 gives $290k of new ACV per ramped salesperson a year [C]. That is 36% of the $800k median quota in the Bridge Group's 2024 SaaS benchmark [S33]. The same report says only 51% of salespeople hit quota. The assumption is deliberately conservative for a company still teaching buyers a new category.

### 7.2 Build (base)

| Year | Salespeople | Effective (ramped) | New customers | Active customers after churn | Obtainable value | Share of SAM |
|---|---|---|---|---|---|---|
| 2027 (year 1) | 4 | 2.0 | 36 | 36 | $1.1M | 0.09% |
| 2028 (year 2) | 8 | 6.0 | 96 | 127 | $3.3M | 0.26% |
| **2029 (year 3)** | 12 | 10.0 | 156 | **264** | **$6.2M** | **0.50%** |
| 2030 (year 4) | 12 | 12.0 | 186 | 410 | $9.3M | 0.74% |
| **2031 (year 5)** | 12 | 12.0 | 186 | **535** | **$11.9M** | **0.95%** |

**By band.**

| Year | 50-199 | 200-999 | 1,000-4,999 | 5,000+ |
|---|---|---|---|---|
| 2029 customers | 74 | 112 | 57 | 20 |
| 2029 value | $0.3M | $1.0M | $2.0M | $3.0M |
| 2031 customers | 154 | 231 | 114 | 37 |
| 2031 value | $0.5M | $2.1M | $3.9M | $5.4M |

In 2031, the top two bands hold 28% of customers but 78% of the SOM value [C].

### 7.3 SOM by case

| Case | Year 3 (2029) | Share of SAM | Year 5 (2031) | Share of SAM |
|---|---|---|---|---|
| Low ACV | $2.7M | 0.44% | $5.3M | 0.85% |
| Base ACV | $6.2M | 0.50% | $11.9M | 0.95% |
| High ACV | $9.7M | 0.51% | $18.6M | 0.99% |

SOM (at most $18.6M) is far below SAM (at least $0.6B), which is below TAM (at least $1.2B). The ordering holds in every case.

---

## 8. Sensitivity

### 8.1 TAM (base $2.5B), one assumption moved at a time

| Assumption moved | Low value | High value | TAM low | TAM high | Effect |
|---|---|---|---|---|---|
| **ACV table (all bands, low to high)** [A1] | Low column | High column | $1.2B | $3.7B | **-50% / +50%** |
| 5,000+ band ACV only [A2] | $60,000 | $250,000 | $2.2B | $2.7B | -11% / +11% |
| India price parity [A3] | India at 50% of table | 100% | $2.1B | $2.5B | -15% / 0% |
| India counts: EPFO <20 share and company factor [A4] | 40% and 0.65 | 10% and 0.95 | $2.2B | $2.7B | -9% / +9% |
| Non-consumer ACV factor [A5] | 30% | 70% | $2.3B | $2.7B | -8% / +8% |
| BI adoption offsets [A6] | US +0, India -20 points | US +15, India -5 points | $2.3B | $2.6B | -5% / +4% |
| US Zipf slope below 500 employees [A7] | 1.0 | 1.1 | $2.3B | $2.6B | -5% / +4% |
| Digital-systems filter [A8] | -10 points | +10 points | $2.4B | $2.5B | -2% / +2% |
| Full rollout, 5,000+ at $1M (founder estimate) | | | | $4.8B | +95% (scenario only) |

**The single assumption that moves the answer most is the ACV table.** It swings TAM by $2.5B, more than all the other assumptions combined.

Within it, the 5,000+ band carries the most weight:

- Its $155,000 base ACV produces 17% of TAM from 0.7% of the companies [C].
- Company-count assumptions, the part most people argue about, move TAM by 5% to 9%.

### 8.2 SAM (base $1.3B)

| Assumption moved | SAM low | SAM high | Effect |
|---|---|---|---|
| ACV table [A1] | $0.6B | $1.9B | -51% / +51% |
| US vertical shares x0.75 / x1.25 [A9] | $1.1B | $1.4B | -12% / +12% |
| India counts [A4] | $1.1B | $1.4B | -10% / +10% |
| Multi-site shares -15 / +15 points [A10] | $1.2B | $1.3B | -7% / +5% |
| India manufacturing share -10 / +10 points [A11] | $1.2B | $1.3B | -4% / +4% |

### 8.3 SOM, year 5 (base $11.9M)

| Assumption moved | SOM low | SOM high |
|---|---|---|
| ACV table [A1] | $5.3M | $18.6M |
| Salespeople from 2029: 8 / 20 [A14] | $9M | $17M |
| Deals per salesperson: 10 / 20 [A15] | $9M | $15M |
| Churn: 25% / 8% [A17] | $10M | $13M |
| Founder deals: 3 / 12 [A16] | $11M | $14M |

SOM is set by sales capacity and price, not by market size. It never exceeds 1% of SAM in any case.

---

## 9. Why now

1. **Decision-making is moving to AI agents.** Gartner predicts that by 2027, 50% of business decisions will be augmented or automated by AI agents for decision intelligence. This was announced 17 June 2025 [S27]. Gartner also predicts 40% of enterprise applications will include task-specific AI agents by 2026, up from under 5% in 2025 [S28].
2. **Reasoning over data is now cheap enough for the mid-market.** Epoch AI measured that the price of a fixed level of LLM capability fell between 9x and 900x per year from 2021 to 2025, depending on the task [S29]. That makes a daily, workspace-wide scan of every metric economically plausible at mid-market price points.
3. **Indian mid-market data is now machine-readable by law.** GST e-invoicing has been mandatory for businesses above ₹5 crore annual turnover since 1 August 2023 (Notification 10/2023-Central Tax) [S19]. Almost every Indian company with 50+ employees now creates structured transaction data, which is the raw material the non-consumption layer needs.
4. **Data-protection rules favour self-hosted and customer-keyed deployments.** India notified the Digital Personal Data Protection Rules in November 2025. The main obligations apply from May 2027 [S30]. Othor AI's on-premise and customer-managed-key options fit buyers who must keep personal data under their own control.
5. **Budgets are growing fastest where GenAI meets data.** Gartner reports data and analytics software grew 13.9% to $175.17B in 2024, driven by cloud, GenAI and new data management capabilities [S22]. It forecasts Indian software spending to grow 17.6% to $24.7B in 2026 [S24].

---

## 10. Expansion markets (outside this TAM)

| Market | Company count | Source | Status |
|---|---|---|---|
| Singapore | 356,100 enterprises in 2024. Non-SMEs (more than S$100M revenue and more than 200 workers) are about 1%, roughly 3,600 companies [C] | SingStat, Singapore Enterprise Landscape 2024 [S32] | Partly sized. Only the non-SME tier is available by size |
| UAE | Not found | No official count of companies by employee band was found | Unsized |
| Saudi Arabia | Not found | No official count of companies by employee band was found | Unsized |

The Middle East and Southeast Asia are adjacent markets. Othor AI's self-hosted deployment and support for multiple LLM providers suit buyers there with data-residency requirements. They are not in the TAM above. Before sizing them, find official establishment counts by employee band: the Saudi General Organization for Social Insurance and the UAE Ministry of Human Resources and Emiratisation are the likely primary sources.

---

## 11. Workings

### 11.1 US counts

A Zipf curve means N(≥ s) = N(≥ 500) x (500 / s)^α.

- Tail exponent from 2007 SUSB [S2]: 1,956 / 18,469 = 0.10591, and α_tail = -log10(0.10591) = **0.975**.
- Exponent below 500 employees: α = **1.06** [S4].
- Check: ln(1,311,698 / 21,041) / ln(50) = ln(62.34) / 3.912 = 4.133 / 3.912 = **1.056** [S1][S3].

| Threshold | Arithmetic | Firms at or above |
|---|---|---|
| 50 | 21,041 x 10^1.06 = 21,041 x 11.48 | 241,600 |
| 200 | 21,041 x 2.5^1.06 = 21,041 x 2.641 | 55,580 |
| 1,000 | 21,041 x 0.5^0.975 = 21,041 x 0.5087 | 10,700 |
| 5,000 | 21,041 x 0.10591 | 2,228 |

Bands:

- 50-199: 241,600 - 55,580 = **186,000**
- 200-999: 55,580 - 10,700 = **44,900**
- 1,000-4,999: 10,700 - 2,228 = **8,480**
- 5,000+: **2,230**

### 11.2 India counts

1. Establishments with 20+ members: (1 - 0.25) x 766,000 = 574,500.
2. Members in those establishments: 73,700,000 - (0.25 x 766,000 x 10) = 71,785,000.
3. Mean size: 71,785,000 / 574,500 = 124.95.
4. Pareto exponent: the mean of a Pareto curve starting at 20 is 20 x α / (α - 1). So α = 124.95 / (124.95 - 20) = **1.191**.

N(≥ s) = 574,500 x (20 / s)^1.191.

| Threshold | Arithmetic | Establishments at or above |
|---|---|---|
| 50 | 574,500 x 0.4^1.191 = 574,500 x 0.3359 | 192,980 |
| 200 | 574,500 x 0.1^1.191 = 574,500 x 0.06448 | 37,040 |
| 1,000 | 574,500 x 0.02^1.191 = 574,500 x 0.009493 | 5,453 |
| 5,000 | 574,500 x 0.004^1.191 = 574,500 x 0.001397 | 802 |

Companies = establishments x 0.8:

| Band | Establishments | Companies |
|---|---|---|
| 50-199 | 155,940 | **124,750** |
| 200-999 | 31,590 | **25,270** |
| 1,000-4,999 | 4,650 | **3,720** |
| 5,000+ | 802 | **642** |

Cross-checks:

- Share of 10+ establishments with 500+: N(≥ 500) = 12,440 and N(≥ 10) = 1,311,000, so 0.95%. AQEES gives 1.4% [S10].
- Companies with 100 to 999 employees: (84,550 - 5,453) x 0.8 = 63,300. Udyam lists 37,042 medium enterprises [S13].

### 11.3 BI adoption curve

1. Median company size of the Eurostat classes:
   - Small (10 to 49): 16.4.
   - Large (250+): about 500.
2. Slope: (68.6 - 23.6) / ln(500 / 16.4) = 45 / 3.417 = **13.17 points per natural-log unit**.
3. Median company size of each band, where half the band's companies are above and half below:
   - 50-199: 50 x (241,600 / 148,600)^(1/1.06) = **79**
   - 200-999: **326**
   - 1,000-4,999: **1,677**
   - 5,000+: 5,000 x 2^(1/0.975) = **10,180**
4. EU rate for 50-199: 23.6 + 13.17 x ln(79 / 16.4) = 23.6 + 13.17 x 1.572 = **44.3%**.
   - US rate: 44.3 + 8 = 52.3%.
   - India rate: 44.3 - 12 = 32.3%.
5. The other bands follow the same arithmetic:

| Band | EU rate | US rate | India rate |
|---|---|---|---|
| 200-999 | 63.0% | 71.0% | 51.0% |
| 1,000-4,999 | 84.5% | 92.5% | 72.5% |
| 5,000+ | 95.0% (capped) | 97.0% (capped) | 83.0% |

### 11.4 TAM, worked example (US, 50-199, base)

- Users: 186,008 x 0.523 = 97,287. Value: 97,287 x $4,800 = **$467.0M**.
- Non-users: 186,008 - 97,287 = 88,721.
- Digital non-users: 88,721 x 0.85 = 75,413. Value: 75,413 x $4,800 x 0.5 = **$181.0M**.
- Band TAM: $467.0M + $181.0M = **$648.0M**.

Every row in section 3 uses the same arithmetic with its own count, adoption rate, digital share and ACV. The model prints each one.

### 11.5 SAM, worked examples

**US manufacturing.**

1. Firms with 100+ employees: 239,265 x (1 - 0.931) = 16,509 [S6].
2. Exponent between 100 and 500: ln(16,509 / 4,177) / ln 5 = **0.854**.

| Threshold | Arithmetic | Firms at or above |
|---|---|---|
| 50 | 16,509 x 2^0.854 | 29,840 |
| 200 | 4,177 x 2.5^0.854 | 9,135 |
| 1,000 | 4,177 x 0.5^0.975 | 2,125 |
| 5,000 | 4,177 x 0.10591 | 442 |

| Band | Raw firms | Dedupe factor | Primary-sector firms |
|---|---|---|---|
| 50-199 | 20,705 | 0.95 | **19,670** |
| 200-999 | 7,009 | 0.85 | **5,958** |
| 1,000-4,999 | 1,683 | 0.70 | **1,178** |
| 5,000+ | 442 | 0.60 | **265** |

**US multi-site operators, 200-999.**

- Remainder: 44,872 - 5,958 = 38,914.
- Multi-site firms: 38,914 x 0.30 x 0.75 = **8,756**.

**Value per company (US, 200-999).**

- (0.710 x $11,000) + (0.290 x 0.92 x 0.5 x $11,000) = $7,810 + $1,467 = **$9,277**.

### 11.6 SOM

1. Effective salespeople = returning salespeople + (new hires x 0.5):
   - 2027: 0 + 4 x 0.5 = 2
   - 2028: 4 + 4 x 0.5 = 6
   - 2029: 8 + 4 x 0.5 = 10
   - 2030 and 2031: 12
2. New customers = effective salespeople x 15 + 6 founder deals:
   - 2027: 36
   - 2028: 96
   - 2029: 156
   - 2030: 186
   - 2031: 186
3. Active customers = previous active x 0.85 + new customers:
   - 2027: 36
   - 2028: 36 x 0.85 + 96 = 126.6
   - 2029: 126.6 x 0.85 + 156 = **263.6**
   - 2030: 263.6 x 0.85 + 186 = 410.1
   - 2031: 410.1 x 0.85 + 186 = **534.6**
4. Value = active customers in each band x expected ACV per deal.
   - Expected ACV per deal (US, 200-999): (0.710 x $11,000 + 0.290 x 0.92 x 0.5 x $11,000) / (0.710 + 0.290 x 0.92) = $9,277 / 0.977 = $9,495.
   - India, same band: $8,527.
   - The average of the two is **$9,011**.

### 11.7 Top-down

- **Fortune Business Insights:** $37.96B x (0.31 x 0.9 + 0.0176) x 0.75 x 0.9 = $37.96B x 0.2966 x 0.675 = **$7.60B**.
- **Grand View Research:**
  - CAGR = (81.45 / 40.1)^(1/8) - 1 = 9.3%.
  - 2026 = $40.1B x 1.093 = $43.8B.
  - Value: $43.8B x (0.37 x 0.9 + 0.0176) x 0.9 = $43.8B x 0.3506 x 0.9 = **$13.83B**.
- **India share of world software:** $24.7B / $1,400B = **1.76%** [S24][S25]. The two figures come from Gartner forecasts of different dates.
- **Implied spend per BI-using company:** $7.60B / 195,545 = $38,900, and $13.83B / 195,545 = $70,700.
- **Othor AI weighted ACV:** Layer 1 of $1.965B / 195,545 = **$10,050**.

### 11.8 Currency

- Rate used: **₹95.80 per USD**. This is the rupee's provisional close on 25 September 2026, reported by PTI via HDFC Sky [S26].
- The same search showed an RBI reference rate of ₹95.7245 on 12 September 2026. The difference does not affect any result.
- The rate is used only to express Indian thresholds in dollars. ₹5 crore = ₹50,000,000 / 95.80 = $0.52M. All ACVs are in USD as supplied.

---

## 12. Assumptions to confirm, ranked by effect

| Rank | ID | Assumption | Base value | Moves the answer by | How to confirm |
|---|---|---|---|---|---|
| 1 | A1 | ACV table by band | As supplied | TAM, SAM and SOM ±50% | Founder sign-off; closed-deal and pilot pricing |
| 2 | A14 to A20 | Sales capacity for SOM | 4 / 8 / 12 salespeople; 15 deals each; 6 founder deals; 15% churn; mix 30 / 45 / 20 / 5; 50-50 country split; 50% first-year productivity | SOM year 5 from $9M to $17M on headcount alone | Founder hiring plan and early win rates |
| 3 | A3 | Same USD ACV in India as in the US | 100% | TAM -15% if India is priced at 50% | India deal pricing to date |
| 4 | A2 | 5,000+ band ACV | $155,000 | TAM ±11% | Enterprise proofs of concept; on-premise quotes |
| 5 | A9 | Vertical shares of the non-manufacturing remainder | US: FS 8%, distribution and logistics 12%, real estate and construction 9%, multi-site pool 30%. India: 12% / 8% / 25% | SAM ±12% | **Replace with SUSB 2022 sector-by-size tables and Economic Census 2022 single-unit and multi-unit tables** |
| 6 | A4 | India: share of EPFO establishments under 20 members; companies per EPFO code | 25%; 0.8 | TAM ±9%; SAM ±10% | EPFO size distribution (annual report tables) or CMIE Prowess |
| 7 | A5 | Non-consumer ACV as a share of band ACV | 50% | TAM ±8% | Pricing of first non-consumer deals |
| 8 | A10 | Share of retail, food and health firms with 2+ establishments | US 45 / 75 / 95 / 100%; India 35 / 65 / 90 / 100% | SAM -7% / +5% | Economic Census 2022 establishment and firm size tables |
| 9 | A6 | BI adoption offsets to the EU curve | US +8 points; India -12 points | TAM -5% / +4% | A US or India BI adoption survey by size band |
| 10 | A7 | US Zipf slope from 50 to 499 employees | 1.06 | TAM -5% / +4% | **SUSB 2022 detailed-size table (first item to verify)** |
| 11 | A11 | India manufacturing share by band | 45 / 45 / 40 / 35% | SAM ±4% | ASI 2023-24 tables by employment size class |
| 12 | A13 | India financial-services count beyond regulator lists | About 300 base-layer NBFCs with 200+ staff; about 300 banks, AMCs and brokers; 11 of 13 reinsurers are foreign branches | SAM about ±1% | RBI and IRDAI entity lists with staff counts |
| 13 | A12 | US manufacturing dedupe factors | 0.95 / 0.85 / 0.70 / 0.60 | SAM about ±2% | SUSB enterprise-industry tables |
| 14 | A8 | Digital-systems share among non-consumers | US 85 / 92 / 97 / 97%; India 75 / 85 / 95 / 95% | TAM ±2% | Survey of target accounts |
| 15 | A21 to A24 | Top-down scaling: US = 90% of North America; India share = software share; 90% of spend from 50+ firms; Fortune software share 75% | As stated | Cross-check only; no effect on TAM | Publisher regional tables |
| 16 | A26 | Adoption ceiling | 95% EU, 97% US | Under 1% | None needed |

---

## 13. Internal sanity check (not for investors)

The founder's long-term target is **$50M to $75M ARR by 2035**.

| Customer mix | Base ACV per customer [C] | Customers for $50M | Customers for $75M | Share of SAM companies | Share of base SAM value |
|---|---|---|---|---|---|
| Salesperson mix (30 / 45 / 20 / 5) | $19,400 | 2,580 | 3,870 | 1.6% to 2.5% | 4.0% to 6.0% |
| Mid-market only (200-999) | $9,010 | 5,550 | 8,320 | 12.9% to 19.3% of the 43,000 SAM companies in that band | 4.0% to 6.0% |
| Enterprise only (1,000+) | $90,900 | 550 | 825 | 5.6% to 8.4% of the 9,860 SAM companies in that band | 4.0% to 6.0% |

**Plain verdict.**

- **The market share is achievable. The assumed sales plan is not enough.**
  - $50M to $75M is 4% to 6% of today's base SAM value. Across the SAM, that is about 1 in 40 to 1 in 60 target companies. For a category leader over ten years, that share is plausible. SAM will also grow by 2035, which this report does not model.
- **The sales plan is the gap.** The 12-person plan in section 7 reaches about $12M of obtainable value by 2031.
  - Holding 2,580 to 3,870 customers at 15% churn means winning 390 to 580 new customers a year.
  - That takes roughly 26 to 39 ramped salespeople at 15 deals each, against the 12 assumed.
  - The alternative is a shift toward 1,000+ employee accounts, where 550 to 825 customers are enough.
- **A pure mid-market strategy needs 13% to 19% of the 200-999 SAM.** That is aggressive.
- **The target is most credible with enterprise weight.** Build an enterprise-weighted mix, and treat the full-rollout pricing (about $1M) as upside, not plan.

---

## 14. Source list

**Access status.** Every source below was read through search-engine extracts because the research environment blocked direct access to most government and publisher sites (see the data-access note). Treat each as "search extract, verify" until someone opens the URL and confirms the figure.

| ID | Title | Publisher | Year | URL | Figure taken |
|---|---|---|---|---|---|
| S1 | Frequently Asked Questions About Small Business 2026 | US SBA Office of Advocacy (from Census SUSB 2022) | 2026 (data 2022) | https://advocacy.sba.gov/wp-content/uploads/2026/02/FINAL_FAQsAboutSmallBusiness_2026_012826.pdf | 21,041 firms with 500+ employees; 6.4 million employer firms; 36,207,130 small businesses; 62.3 million small-business employees (45.9% of private workers) |
| S2 | Statistics about business size (archived census.gov/econ/smallbus.html) | US Census Bureau, via UNT Web Archive | 2007 data | https://webarchive.library.unt.edu/web/20121019014834mp_/http://www.census.gov/econ/smallbus.html | 18,469 firms with 500+ employees; 1,956 firms with 5,000+ |
| S3 | How Many Businesses Are There in America and What Does it Mean for Employee Ownership? | Certified EO (quoting SUSB) | SUSB 2019 data | https://www.certifiedeo.com/blog-posts/how-many-businesses-are-there-in-america-and-what-does-it-mean-for-employee-ownership | 1,311,698 firms with 10+ employees; 1,108 + 582 + 540 firms at 5,000+ (secondary; cross-check only) |
| S4 | Zipf Distribution of U.S. Firm Sizes (Axtell, R.) | Science 293(5536) | 2001 | https://www.science.org/doi/10.1126/science.1062081 | US firm sizes follow Zipf with exponent about 1.06 |
| S5 | 2022 SUSB Annual Data Tables by Establishment Industry | US Census Bureau | 2025 release (2022 data) | https://www.census.gov/data/tables/2022/econ/susb/2022-susb-annual.html | Not opened. Use it to replace the modelled US band counts |
| S6 | Facts About Manufacturing | National Association of Manufacturers (from SUSB 2022) | 2022 data | https://nam.org/mfgdata/facts-about-manufacturing-expanded/ | 239,265 manufacturing firms; 4,177 with 500+; 93.1% under 100 employees |
| S7 | Establishment, firm, or enterprise: does the unit of analysis matter? | US BLS, Monthly Labor Review | 2016 | https://www.bls.gov/opub/mlr/2016/article/establishment-firm-or-enterprise.htm | About 294,000 multi-location firms owning 2.3 million establishments |
| S8 | Employers up 6.6% at 766,000; members rise 7.6% in FY24: EPFO report | Business Standard (from EPFO Annual Report 2023-24) | 2024 (FY2023-24 data) | https://www.business-standard.com/economy/news/employers-up-6-6-at-766-000-members-rise-7-6-in-fy24-epfo-report-124111101101_1.html | 766,000 contributing establishments; 73.7 million contributing members |
| S9 | Employees' Provident Funds and Miscellaneous Provisions Act, 1952 | EPFO, Government of India | 1952, as amended | https://www.epfindia.gov.in/ | The Act applies to establishments with 20+ employees |
| S10 | Report on Fourth Round (January to March 2022) of Quarterly Employment Survey | Labour Bureau, via PIB | 2022 | https://www.pib.gov.in/PressReleaseIframePage.aspx?PRID=1862597 | 1.4% of establishments have 500+ workers; about 80% have 10 to 99; worker shares: manufacturing 38.5%, education 21.7%, IT/BPO 12%, health 10.6%, trade 5.3%, transport 4.6% |
| S11 | Annual Survey of Industries (ASI) Results for 2023-24 | MoSPI, via PIB | 2025 (2023-24 data) | https://www.pib.gov.in/PressReleasePage.aspx?PRID=2161192 | 260,061 factories |
| S12 | India's factories | Data For India | 2025 to 2026 (2023 data) | https://www.dataforindia.com/factories/ | One in five factories employed 100+ workers by 2023 |
| S13 | India MSME Statistics 2026 (Udyam) | DataRank India (secondary). Total registrations: PIB, 28 February 2026 | Snapshot date not stated; PIB 2026 | https://datarankindia.com/india-msme-statistics/ and https://www.pib.gov.in/PressReleasePage.aspx?PRID=2246892 | 37,042 medium enterprises out of about 47.2 million registrations; 78.3 million enterprises on Udyam and UAP as of 28 February 2026 |
| S14 | IRDAI Annual Report 2024-25 | Insurance Regulatory and Development Authority of India (hosted by Life Insurance Council) | 2025 (data at 31 March 2025) | https://lifeinscouncil.org/component/IRDAI%20Annual%20Report%202024-25.pdf | 74 insurers: 26 life, 25 general, 8 standalone health, 2 specialised, 13 reinsurers |
| S15 | NBFC sector data, 31 March 2025 (RBI), as reported | Business Standard and Outlook Business, citing RBI | 2025 | https://www.business-standard.com/finance/news/nbfc-asset-quality-worsens-to-5-9-amid-rising-write-offs-rbi-fsr-125063001232_1.html and https://www.outlookbusiness.com/explainers/explained-rbi-expands-upper-layer-nbfc-list-and-what-it-means-for-indias-credit-system | About 9,000 NBFCs; 15 upper-layer; 656 middle-layer |
| S16 | Digital economy and society statistics: enterprises | Eurostat, Statistics Explained | 2023 data | https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Digital_economy_and_society_statistics_-_enterprises | Data analytics by own employees: 28.2% of enterprises; small 23.6%; large 68.6% |
| S17 | How digitalised have the EU's enterprises become? | Eurostat news | 2024 (2023 data) | https://ec.europa.eu/eurostat/web/products-eurostat-news/w/ddn-20240829-1 | ERP: 37.9% of small to 86.3% of large enterprises; CRM: 22% to 61% |
| S18 | 67% of Indian MSMEs demonstrate digital readiness: CMR study | DQ India | 2025 | https://www.dqindia.com/news/67-of-indian-msmes-demonstrate-digital-readiness-cmr-study-9402460 | 67% of MSMEs digitally equipped; 43% competent in ERP and cloud |
| S19 | Notification 10/2023-Central Tax, dated 10 May 2023 | GST Council / CBIC | 2023 | https://www.gstcouncil.gov.in/node/4365 | E-invoicing mandatory above ₹5 crore turnover from 1 August 2023 |
| S20 | Business Intelligence Market Size, Share and Growth, 2034 | Fortune Business Insights | 2026 edition | https://www.fortunebusinessinsights.com/business-intelligence-bi-market-103742 | $34.82B (2025); $37.96B (2026); $72.21B (2034); CAGR 8.40%; North America 31.00% |
| S21 | Business Intelligence Software Market Report, 2026-2033 | Grand View Research | 2026 | https://www.grandviewresearch.com/industry-analysis/business-intelligence-software-market and https://www.grandviewresearch.com/press-release/global-business-intelligence-software-market | $40.1B (2025); $81.45B by 2033; North America 37% |
| S22 | Market Share Alert: Data and Analytics Software Grows 14% in 2024; Market Share: Analytic Platforms, Worldwide, 2024 | Gartner | 2025 (2024 data) | https://www.gartner.com/en/documents/6727134 and https://www.gartner.com/en/documents/6537402 | Data and analytics software $175.17B (+13.9%); analytic platforms $41.92B (+17.3%) |
| S23 | BI market pages | Mordor Intelligence; Polaris Market Research; Precedence Research; The Business Research Company | 2025 | https://www.mordorintelligence.com/industry-reports/global-business-intelligence-bi-vendors-market-industry ; https://www.polarismarketresearch.com/industry-analysis/business-intelligence-market ; https://www.precedenceresearch.com/business-intelligence-software-market ; https://www.thebusinessresearchcompany.com/report/bi-software-global-market-report | $37.73B; $35.30B; $47.04B; $85.65B (2025) |
| S24 | Gartner Forecasts India IT Spending to Exceed $176 Billion in 2026 | Gartner | 18 November 2025 | https://www.gartner.com/en/newsroom/press-releases/2025-11-18-gartner-forecasts-india-it-spending-to-exceed-176-billion-us-dollars-in-2026 | India software spending $24.7B in 2026 (+17.6%) |
| S25 | Gartner Forecasts Worldwide IT Spending to Grow 10.8% in 2026, Totaling $6.15 Trillion | Gartner | 3 February 2026 | https://www.gartner.com/en/newsroom/press-releases/2026-02-03-gartner-forecasts-worldwide-it-spending-to-grow-10-point-8-percent-in-2026-totaling-6-point-15-trillion-dollars | Worldwide software spending above $1.4 trillion in 2026 |
| S26 | Rupee gains 19 paise to close at 95.80 against dollar | HDFC Sky (PTI) | 25 September 2026 | https://hdfcsky.com/news/inr-vs-usd-rate-september-25-2026 | ₹95.80 per USD |
| S27 | Gartner Announces the Top Data and Analytics Predictions | Gartner | 17 June 2025 | https://www.gartner.com/en/newsroom/press-releases/2025-06-17-gartner-announces-top-data-and-analytics-predictions | By 2027, 50% of business decisions augmented or automated by AI agents |
| S28 | Gartner Predicts 40% of Enterprise Apps Will Feature Task-Specific AI Agents by 2026 | Gartner | 26 August 2025 | https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025 | 40% by 2026, from under 5% in 2025 |
| S29 | LLM inference prices have fallen rapidly but unequally across tasks | Epoch AI | 2025 | https://epoch.ai/data-insights/llm-inference-price-trends | Price for fixed capability fell 9x to 900x per year |
| S30 | Digital Personal Data Protection Rules, 2025 | PIB, Government of India | November 2025 | https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190014 | Rules notified; 18-month phased compliance |
| S31 | Zinnov-nasscom India GCC Landscape Report 2026 | Zinnov and nasscom | 2026 | https://zinnov.com/centers-of-excellence/zinnov-nasscom-india-gcc-landscape-2026-report/ | 2,117 GCCs; 2.36 million staff; 506 Forbes Global 2000 companies |
| S32 | Singapore Enterprise Landscape | Singapore Department of Statistics | 2024 data | https://www.singstat.gov.sg/infographics/singapore-enterprise-landscape | 356,100 enterprises; non-SMEs about 1% |
| S33 | 2024 SaaS AE Metrics and Compensation Benchmark | The Bridge Group | 2024 | https://blog.bridgegroupinc.com/2024-ae-metrics-compensation-benchmark | Median quota about $800k; median ACV $47k; 51% of salespeople hit quota |
| S34 | Compendium of U.S. Health Systems | AHRQ | 2023 data | https://www.ahrq.gov/chsp/data-resources/compendium-2023.html | 639 health systems; 6,800 hospitals (context for the multi-site health segment) |
| S35 | ACV table and full-rollout estimate | Othor AI (company-supplied) | 2026 | Internal | Band ACVs [A1]; about $1M full-rollout estimate |

---

## 15. Slide extract

**Headline.** Othor AI addresses a **$2.5B** annual market across 396,000 companies in India and the US. **$1.3B** of it sits in its priority verticals, and an assumed 12-person sales team can reach **$6.2M by year 3 and $11.9M by year 5**.

**Definitions.**

- **TAM ($2.5B):** annual software value if every company with 50+ employees in India and the US that uses BI, or runs on digital systems without BI, bought Othor AI at its size-band price.
- **SAM ($1.3B):** the part of TAM in Othor AI's current verticals (manufacturing, insurance and financial services, distribution and logistics, real estate and construction, multi-site operators) and size filters.
- **SOM ($6.2M year 3; $11.9M year 5):** the annual contract value an assumed sales team could win and keep, derived from sales capacity, not picked as a percentage.

**Non-consumption insight.** 163,000 companies (41% of the universe) run on ERP, CRM or accounting systems but have no BI. Because Othor AI needs no data team and no predefined KPIs, they become buyers. They add $0.5B that no BI market report counts.

**Method.** Bottom-up company counts by size band (US Census SUSB, India EPFO), times Othor AI's price per band, split into current BI users and digital non-consumers, then cross-checked against two published BI market estimates.

**Why now.**

- By 2027, 50% of business decisions will be augmented or automated by AI agents (Gartner, June 2025).
- Since August 2023, every Indian business above ₹5 crore turnover must issue machine-readable e-invoices (GST Notification 10/2023).

| Measure | Base | Range | Source basis |
|---|---|---|---|
| Companies in universe (50+ employees, India plus US) | 396,000 | Tested range up to -33% / +39% (India, 50-199) | SUSB 2022; EPFO FY2023-24 |
| TAM | $2.5B | $1.2B to $3.7B | Counts x ACV, two layers |
| of which non-consumption | $0.5B | $0.3B to $0.7B | 163,000 digital companies without BI |
| SAM | $1.3B | $0.6B to $1.9B | Priority verticals and size filters |
| SOM year 3 / year 5 | $6.2M / $11.9M | $2.7M to $18.6M | Assumed 4 to 12 salespeople |
| Existing BI wallet, India plus US (top-down) | $7.6B to $13.8B | Two publishers | Fortune Business Insights; Grand View Research |
