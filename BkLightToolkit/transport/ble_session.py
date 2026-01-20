from bleak import BleakClient, BleakScanner
from typing import Optional

UUID_WRITE = "0000fa02-0000-1000-8000-00805f9b34fb"
UUID_NOTIFY = "0000fa03-0000-1000-8000-00805f9b34fb"
HANDSHAKE = bytes.fromhex("08 00 01 80 0E 06 32 00")

class BLETransport:
    """
    Gestionnaire BLE pour un panneau : connexion, envoi et réception de données.
    """
    def __init__(self, address: str, mtu: int = 512, log: bool = False) -> None:
        """
        Initialise le transport BLE.

        Args:
            address (str): Adresse BLE du panneau.
            mtu (int, optional): Taille maximale des paquets. Defaults to 512.
            log (bool, optional): Active les logs BLE. Defaults to False.
        """
        self.address = address
        self.client: Optional[BleakClient] = None
        self.mtu = mtu
        self.log = log

    async def connect(self) -> None:
        """
        Établit la connexion avec le périphérique BLE et démarre la notification.
        """
        device = await BleakScanner.find_device_by_address(self.address, timeout=5)
        if device is None:
            raise Exception(f"Device {self.address} not found")

        self.client = BleakClient(device)
        await self.client.connect()
        await self.client.start_notify(UUID_NOTIFY, self._handler)
        if self.log:
            print(f"Connected to {self.address}")

    async def _handler(self, data: bytearray) -> None:
        """
        Gestionnaire des notifications reçues depuis le panneau.

        Args:
            data (bytearray): Données reçues.
        """
        if self.log:
            print("NOTIF:", data.hex())

    async def send(self, data: bytes) -> None:
        """
        Envoie des données au panneau. Connecte automatiquement si nécessaire.

        Args:
            data (bytes): Données à envoyer.
        """
        if self.client is None or not self.client.is_connected:
            await self.connect()
        await self.client.write_gatt_char(UUID_WRITE, HANDSHAKE + data, response=True)
