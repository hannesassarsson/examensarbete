# Examensarbete – Incheckningssystem med NFC och display (Rock 4C+)

Detta projekt har utvecklats som examensarbete inom mjukvaruutveckling för inbyggda system. Systemet registrerar närvaro genom NFC-tagg och visar status på en touchskärm. Projektet är byggt med fokus på embedded-lösningar, lokal datalagring och modern webbteknologi.

---

## Funktioner

- Inloggning med NFC-tagg + PIN-kod
- Touchskärmsgränssnitt med React
- Incheckningsstatus i realtid
- Incheckningshistorik
- Ändring av PIN-kod
- JWT-skyddad autentisering
- Backend byggd med Flask och SQLite
- Automatisk visning av dagens schema (Google Calendar)
- Planerat: Ansiktsigenkänning via CSI-kamera

---

## Mjukvarustruktur

```plaintext
exam-project/
├── backend/
│   ├── app.py
│   ├── database/
│   │   └── db.sqlite
│   ├── credentials/
│   │   └── service_account.json
│   └── hardware/
│       ├── nfc/
│       │   └── nfc_reader.py
│       ├── display/
│       │   └── display_manager.py
│       └── camera/
│           └── face_recognition.py
│
├── frontend/
│   ├── components/
│   │   └── [React-komponenter]
│   └── main.jsx
│
└── requirements.txt
```

---

## Installation och körning

### Backend (Flask + SQLite + NFC)

```bash
# Klona projektet
cd backend
pip install -r ../requirements.txt

# Kör backendserver
python3 app.py
```

### Frontend (React)

```bash
cd frontend
npm install
npm run dev -- --host
```

---

## Hårdvara

- Rock 4C+ (eller Rock 5 Model B)
- PN532 NFC-läsare via I2C/UART
- 7" HDMI-touchskärm (visar React UI)
- (Valfritt) CSI-kamera för ansiktsigenkänning

---

## Bibliotek och teknologier

- Python 3.11+
- Flask
- SQLite
- Adafruit CircuitPython (NFC + Display)
- React + Bootstrap
- JWT (PyJWT)
- face_recognition (planerat)
- Google Calendar API

---

## Säkerhet

- JWT-token för autentisering
- PIN-kod krypteras (framtida tillägg)
- NFC-ID lagras internt för inloggning

---

## Kontakt

Utvecklat av **Hannes Assarsson**  
E-post: hannesassarsson02@gmail.com

---

## Exempelbilder och översikter

- Systemöversikt (flödesschema)
- Skärmbild från incheckning
- Illustration av Rock 4C+ och NFC-läsare

*(Se bilagda filer i rapport eller GitHub)*
