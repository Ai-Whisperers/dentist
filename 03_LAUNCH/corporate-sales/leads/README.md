## PRICING CROSS-REFERENCE (June 2026)

> Service prices in this document are NOT authoritative. The master reference is:
> `00_STRATEGIC/financial-pricing/canonical-pricing-reference-v2.md`
>
> Any price update should happen in the canonical file only.

---

# Lead Databases

## Lead Analysis Documents

| File | Segment | Leads | Source |
|------|---------|-------|--------|
| `lead-prioritization-analysis.md` | Gym/Spa/Estetica/Depilation | 238 | Paraguay beauty/wellness DB |
| `premium-leads-analysis.md` | IT/Finance/Legal/Medical/Edu/Real Estate | 326 | Google Maps scrape |

## Lead CSV Files

### Gym/Spa Segment
- `gym-spa-leads.csv` — 638 gym/spa/beauty businesses, scored and tier-labeled (A/B/C)

### Premium Segment
- `premium-leads.csv` — 326 IT/Finance/Legal/Medical/Edu/Real Estate businesses, scored and tier-labeled (A/B/C)

## Scoring Methodology

### Gym/Spa (0–100 scale)
- Review volume: 0–30 pts (proxy for business size)
- Website presence: 0–15 pts
- Rating 4.5+: 0–10 pts
- Category match (gym/health): 0–10 pts
- Asunción location: 0–5 pts

### Premium Segment (0–100 scale)
- Premium vertical (tech/consulting/legal/finance): +25 pts
- Reviews 200+: +30 pts, 100+: +25 pts, 50+: +20 pts, 20+: +10 pts
- Rating 4.8+: +15 pts, 4.5+: +10 pts, 4.0+: +5 pts
- Phone: +5 pts, Website: +5 pts
