# DENTIST CONTENT REPO

## Status
Deploy-ready content package currently parked at `Ai-Whisperers/dentist`.

## Build surface
No app code in this repo. Composed web output requires a separate front-end branch or an Ai-Whisperers deployment hook.

## Pages authored
- Home/hero + stats + reasons
- Services + general/cosmetic/rehab tabs
- Pricing
- Second opinion
- Treatment planning
- About
- Expat landing
- FAQ (20 Q each)
- Testimonials (8-9)
- Contact
- Blog config

### Schema Hooks (content ready)
- `content/*/ld-localbusiness.json`
- `content/*/ld-faq.json`
- `content/*/ld-reviews.json`

## Next options
1. Agent wires JSON content into a Next.js static branch under `Ai-Whisperers/client-site-*`.
2. Agent publishes JSON-only drafts as review deliverables.
3. Agent pins this branch as source-of-truth for a future build sprint.
