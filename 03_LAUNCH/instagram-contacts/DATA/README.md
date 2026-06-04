# DATA/

## Files

| File | Rows | Description |
|------|-----:|-------------|
| `instagram-contacts-merged.csv` | 83,796 | Deduped IG followers from 4 dental clinic scrapes |
| `contacts-scored.csv` | 74,062 | All human contacts, scored (name_score, expat_signal, professional_signal, asuncion_signal, outreach_score, outreach_tier) |
| `contacts-premium.csv` | 16,220 | Tier A (score >= 60) — best outreach candidates |
| `contacts-segmented.csv` | summary | Tier breakdown + top samples |
| `influencers-paraguay-500.csv` | 296 | Top Paraguay influencers (IG + TikTok + YouTube + Twitter) |

## Scoring Columns (contacts-scored.csv / premium.csv)

| Column | Description |
|--------|-------------|
| `name_score` | 0-100. High for proper multi-word name + firstname_lastname username pattern |
| `expat_signal` | 0/1/2. Higher for European characters in name or expat first name in username |
| `professional_signal` | 0/2. Triggered by Dr/Dra/Lic/Ing/Abog in name or username |
| `asuncion_signal` | 0/2. Higher for Asunción/py/luque/encarnacion in username or name |
| `outreach_score` | Sum of above, capped at 100 |
| `outreach_tier` | A (60+), B (35-59), C (20-34), D (<20) |

## Tier A Sample (top 5 by score)
```
benitez_hugojavier - Hugo Javier Benítez - 100
andy_agcl - Andrea Centurion - 100
kevin_laneri - Kevin Laneri - 100
mvictoria_ss - María Victoria Sánchez - 100
rosangela_oliverrodrigues - Rosangela Rodrigues Oliveira - 100
```

## Sources
- protectiondentalcenter (66K followers scraped)
- odontologia3py (9K)
- odontospy (8K)
- embaparuk (477)
