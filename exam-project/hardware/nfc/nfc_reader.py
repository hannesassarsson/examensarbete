import board
import busio
from digitalio import DigitalInOut
from adafruit_pn532.i2c import PN532_I2C

class NFCReader:
    def __init__(self):
        try:
            i2c = busio.I2C(board.SCL, board.SDA)
            self.pn532 = PN532_I2C(i2c, debug=False)
            self.pn532.SAM_configuration()
            print("[NFC] PN532 initialiserad.")
        except Exception as e:
            print(f"[NFC] Initieringsfel: {e}")
            self.pn532 = None

    def read_uid(self):
        if self.pn532 is None:
            return None

        uid = self.pn532.read_passive_target(timeout=0.5)
        if uid:
            return ''.join([format(byte, '02X') for byte in uid])
        return None
