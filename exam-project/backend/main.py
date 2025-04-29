import requests
import time

nfc_id = "04:A3:21:EF:56:99"  # Simulerat ID
pin = "1234"                  # Test-PIN

while True:
    print("🔄 Simulerar inloggning...")
    
    # 1. Logga in
    login_response = requests.post("http://localhost:3000/api/login", json={"pin": pin})
    token = login_response.json().get("token")

    if not token:
        print("❌ Kunde inte logga in.")
        break

    # 2. Skicka checkin
    checkin_response = requests.post(
        "http://localhost:3000/api/checkin",
        headers={"Authorization": f"Bearer {token}"},
        json={}
    )
    print(checkin_response.json())

    time.sleep(10)  # vänta 10 sekunder innan nästa "tag"