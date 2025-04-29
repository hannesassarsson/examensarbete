from hardware.nfc.nfc_reader import NFCReader
import requests
import time

# Create an instance of the NFCReader class
nfc_reader = NFCReader()

# Infinite loop to continuously check for NFC tags
while True:
    # Waiting for an NFC tag
    print("Waiting for an NFC tag...")
    
    # Read NFC tag
    nfc_id = nfc_reader.read_nfc()
    
    # If NFC tag is detected
    if nfc_id:
        # Detected NFC tag ID
        print(f"Detected tag: {nfc_id}")
        
        # Send NFC tag ID to server
        response = requests.post("http://localhost:3000/api/checkin", json={"nfc_id": nfc_id})
        
        # Server response
        print(response.json())
    
    # Delay before next check
    time.sleep(1)