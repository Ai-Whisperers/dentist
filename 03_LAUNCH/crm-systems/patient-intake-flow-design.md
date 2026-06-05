## PRICING CROSS-REFERENCE (June 2026)

> Service prices in this document are NOT authoritative. The master reference is:
> `00_STRATEGIC/financial-pricing/canonical-pricing-reference-v2.md`
>
> Any price update should happen in the canonical file only.

---

# DIGITAL PATIENT INTAKE FLOW
## Dra. GP - Pre-Appointment Medical History
**Version:** 1.0 - June 2026

---

## PURPOSE

Collect patient medical history BEFORE the appointment. This means:
- No waiting room paperwork
- Patient completes at their own pace before arriving
- Better use of appointment time (she reviews beforehand)
- More thorough than paper forms (people type more than write)

---

## OPTION 1: GOOGLE FORM (Recommended)

Create a Google Form and send link via WhatsApp when appointment is confirmed.

GOOGLE FORM QUESTIONS:

SECTION 1: Personal Information
- Full name
- Date of birth
- Phone / WhatsApp number
- Email (optional - for sending reports)
- How did you hear about us? (dropdown: Google, WhatsApp, Friend/Family, Other dentist, Other)

SECTION 2: Medical History

- Do you have any medical conditions? (checkboxes: Diabetes, Hypertension, Heart disease, Thyroid problems, Bleeding disorder, Cancer, HIV, Hepatitis, None)
- Are you currently taking any medications? (text: write none if not taking any)
- Do you have any allergies? (text: medications, latex, other)
- Have you had any surgeries or hospitalizations in the last 5 years? (yes/no + details)
- Do you smoke? (yes/no/how much)
- Do you drink alcohol? (yes/no/how often)

SECTION 3: Dental History

- What is the main reason for your visit today? (text)
- Are you experiencing pain right now? (yes/no/level 1-10)
- Have you had dental treatment before? (yes/no/if yes, what)
- Do you have any ongoing dental issues? (text)
- Have you had X-rays recently? (yes/no/if yes, can you bring them?)
- Are you afraid of dental treatment? (yes a little/yes a lot/not really)

SECTION 4: Insurance / Payment

- Do you have dental insurance? (yes/no)
- If yes, insurance company name: (text)
- Preferred payment method: (cash/transfer/Pagopar)

FORM LINK: [INSERT GOOGLE FORM LINK AFTER CREATING]

---

## OPTION 2: WHATSAPP-BASED INTAKE (If they prefer WhatsApp)

Send this message after appointment confirmation:

"Hola [NAME]! Confirmando tu turno para [DATE] a las [TIME].

Antes de venir, te mando unas preguntas rapidas para preparar la consulta. Esto me ayuda a aprovechar mejor el tiempo contigo.

Respondeme por WhatsApp:

1. Tenes alguna enfermedad cronica? (diabetes, presion alta, etc)
2. Tomas algun medicamento regularmente?
3. Tenes alergias a medicamentos o latex?
4. Estas experimentando dolor ahora mismo? (si/no y nivel 1-10)
5. Cual es el motivo de tu consulta?

Opcional: si prefieres, podes llenar el formulario online: [LINK]

---

## AUTOMATION WITH HERMES AGENT

When patient confirms appointment via WhatsApp, Hermes sends:

"Perfecto [NAME]! Tu turno queda confirmado para [DATE] a las [TIME] en [LOCATION].

Antes de venir, te mando un formulario rapido para prepararte. Takes about 5 minutes:

[GOOGLE FORM LINK]

Si preferis responder por WhatsApp, te mando las preguntas ahora."

---

## AFTER COMPLETION

When patient submits form or responds via WhatsApp:

1. Hermes Agent receives response
2. Agent logs in CRM (Spreadsheet row: Name, Date, Intake status: COMPLETE)
3. Agent flags if any RED FLAGS in medical history (allergies, bleeding disorder, etc.)
4. Dra. GP reviews before appointment

RED FLAGS TO FLAG:
- Bleeding disorder (need to check before any procedure)
- Heart condition / heart murmur (need antibiotic prophylaxis)
- Diabetes (uncontrolled - may need medical clearance)
- Allergies to medications listed
- Currently taking blood thinners
- HIV status disclosed (handle with care protocol)

Hermes message to Dra. GP if red flag:

"[PATIENT NAME] confirmed. Medical history has [RED FLAG]. Review before appointment."

---

## GOOGLE FORM SETUP INSTRUCTIONS

1. Go to Google Forms
2. Create new form named "DraGP - Patient Intake"
3. Add sections as above
4. Set to collect emails (optional)
5. Set to NOT require sign-in (so patients can open directly)
6. Copy form link
7. Replace [GOOGLE FORM LINK] in message templates above

SHARE THE LINK VIA:
- WhatsApp directly
- Appointment confirmation message
- Email if patient provides email

---

**Created:** June 2, 2026
