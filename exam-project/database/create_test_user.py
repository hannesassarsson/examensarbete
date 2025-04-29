from db_manager import DatabaseManager

# Initiera databasen
db = DatabaseManager("db.sqlite")

# Enkel testanvändare
name = "Testanvändare"
pin = "1234"
nfc_id = "ABC123"

# Lägg till i databasen
db.add_user(name, pin, nfc_id)

print(f"✅ Användare '{name}' med PIN '{pin}' och NFC-ID '{nfc_id}' har lagts till.")