## PRICING CROSS-REFERENCE (June 2026)

> Service prices in this document are NOT authoritative. The master reference is:
> `00_STRATEGIC/financial-pricing/canonical-pricing-reference-v2.md`
>
> Any price update should happen in the canonical file only.

---

# QR CODE SYSTEM
## Dra. Gabriella González Pane
**Version:** 1.0 — June 2026

---

## PURPOSE

QR codes that patients can scan to: message WhatsApp, leave Google review, save contact, or visit website. Place codes throughout the office and on materials.

---

## QR CODES TO CREATE

### QR 1: WhatsApp Direct Message
```
https://wa.me/595981146759?text=Hola%20Dra.%20GP
```
**Where:** Business cards, counter, waiting area, website
**What it does:** Opens WhatsApp with pre-filled message

---

### QR 2: WhatsApp — Specific Message (Second Opinion)
```
https://wa.me/595981146759?text=Hola!%20Me%20interesa%20una%20segunda%20opinión%20odontológica
```
**Where:** Expat forums, referral cards
**What it does:** Opens WhatsApp with second opinion inquiry

---

### QR 3: Google Review
```
https://g.page/[YOUR_PLACE_ID]/review
```
**Where:** After-treatment instructions, counter, WhatsApp follow-up
**What it does:** Opens Google review form for your business

---

### QR 4: Save Contact (vCard)
```
https://play.google.com/store/apps/details?id=com.application.contact2
```
No — use a direct link to a .vcf file hosted on your site:

```
https://[YOURDOMAIN]/contact/dra-gp.vcf
```
**Where:** Everywhere
**What it does:** Clicking saves contact to phone

---

### QR 5: Website
```
https://[YOURDOMAIN]
```
**Where:** Business cards, letterhead, signage
**What it does:** Opens website

---

## HOW TO CREATE QR CODES

Use free tools:
1. **QR Code Generator** (qrcode-monkey.com) — free, no signup
2. **Canva** — includes QR code designer
3. **Chrome Extension:** "QR Code Generator"

### Settings:
- Error correction: HIGH (30%)
- Size: 1024×1024 px minimum
- Format: PNG or SVG
- Color: Black (not colored — more reliable scanning)

---

## WHERE TO PLACE QR CODES

| Location | QR Code | Purpose |
|----------|---------|---------|
| Counter/reception | QR 1 (WhatsApp) | Contact easily |
| Inside treatment room | QR 1 (WhatsApp) | Post-treatment follow-up |
| On business card | QR 1 (WhatsApp) | Direct message |
| On business card | QR 3 (Google Review) | Leave review |
| On consent form | QR 1 (WhatsApp) | Questions after |
| On post-treatment sheet | QR 1 (WhatsApp) | Post-treatment issues |
| On referral card | QR 2 (Second Opinion) | Drive second opinions |
| On letterhead | QR 1 (WhatsApp) | Contact |

---

## PRINT SPECIFICATIONS

| Location | Size | Material |
|----------|------|----------|
| Business card | 15×15mm | Same as card |
| Counter card (standing) | 50×50mm | Glossy cardstock |
| Wall/poster | 100×100mm | Matte laminate |
| Sticker (equipment) | 20×20mm | Waterproof sticker |

---

## QR CODE TRACKING

Track which QR codes get scanned:
- Use QR code generator with UTM parameters
- Example: `https://wa.me/595XXX?utm_source=business-card&utm_medium=qr&utm_campaign=second-opinion`

But for now, simple counting is fine.

---

## SAMPLE QR STICKER TEXT

```
┌──────────────────────┐
│                      │
│   [QR CODE]          │
│                      │
│  Escaneá para         │
│  escribirnos          │
│                      │
│  ⏱️ Respuesta en     │
│  menos de 24h         │
│                      │
└──────────────────────┘
```

---

**STATUS:** Create these QR codes when business WhatsApp number is confirmed.