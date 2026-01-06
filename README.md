# Examensarbete – In- och utcheckningssystem

Detta repository innehåller mitt examensarbete inom utbildningen **Mjukvaruutvecklare Inbyggda System** (examen maj 2025).

Projektet är ett komplett in- och utcheckningssystem med fokus på **systemutveckling, säkerhet och användarflöden**, där både mjukvara och hårdvara ingår. Lösningen är byggd för att efterlikna ett verkligt produktionssystem snarare än ett rent skolprojekt.

---

## Översikt

Systemet möjliggör in- och utcheckning av användare via:
- NFC
- PIN-kod
- Ansiktsigenkänning (kamera)

Lösningen består av:
- Backend med REST API
- Frontend anpassad för touchskärm
- Databas för användare, historik och status
- Integration med inbyggd hårdvara

Projektet är utvecklat end to end, från systemdesign och arkitektur till implementation, testning och dokumentation.

---

## Funktionalitet

- Inloggning via NFC och PIN
- In- och utcheckning med tidsloggning
- Visning av incheckningsstatus
- Historik per användare
- Säker autentisering med JWT
- Touchanpassat gränssnitt
- Kommunikation mellan frontend och backend via REST API

---

## Systemarkitektur

Systemet är uppdelat i tydliga lager:

- **Frontend**
  - Byggd i React
  - Anpassad för touchskärm
  - Kommunicerar med backend via REST API

- **Backend**
  - Python (Flask)
  - Hanterar affärslogik, autentisering och databasåtkomst
  - JWT används för säker sessionhantering

- **Databas**
  - SQLite
  - Lagrar användare, incheckningshistorik och status

- **Hårdvara**
  - Rock 4C+
  - NFC-läsare
  - Kamera
  - Touchskärm

---

## Tekniker och verktyg

- Python
- Flask
- React
- JavaScript
- REST API
- SQLite
- JWT
- Linux
- Git
- NFC
- Kamera (CSI)

---

## Syfte med projektet

Syftet med examensarbetet var att:
- visa förståelse för systemutveckling i inbyggda miljöer
- kombinera hårdvara och mjukvara i ett sammanhängande system
- arbeta med säkerhet, användarflöden och arkitektur
- bygga en lösning som liknar verkliga produktionssystem

---

## Status

Projektet är färdigställt som examensarbete och godkänt med betyget **VG**.  
Vidareutveckling och förbättringar är möjliga, exempelvis:
- utökad behörighetshantering
- förbättrad UI
- loggning och analys

---

## Författare

**Hannes Assarsson**  
Mjukvaruutvecklare  
Examen maj 2025  

📧 hannesassarsson02@gmail.com  
🌐 https://hannesassarsson.github.io/portfolio/