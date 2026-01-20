from PIL import Image, ImageDraw, ImageFont
from ..transport.ble_session import BLETransport
from typing import Tuple

class Panel:
    """
    Représente un panneau individuel et gère le rendu et l'envoi des données.
    """
    def __init__(self, address: str, tile_width: int = 32, tile_height: int = 32, log: bool = False) -> None:
        """
        Initialise un panneau avec son adresse BLE et ses dimensions.

        Args:
            address (str): Adresse BLE du panneau.
            tile_width (int, optional): Largeur du panneau en pixels. Defaults to 32.
            tile_height (int, optional): Hauteur du panneau en pixels. Defaults to 32.
            log (bool, optional): Active les logs BLE. Defaults to False.
        """
        self.address = address
        self.transport = BLETransport(address, log=log)
        self.tile_width = tile_width
        self.tile_height = tile_height

    def _render_text(self, text: str, color: Tuple[int,int,int] = (255,255,255)) -> Image.Image:
        """
        Convertit du texte en image RGB adaptée au panneau.

        Args:
            text (str): Texte à afficher.
            color (Tuple[int,int,int], optional): Couleur du texte. Defaults to blanc.

        Returns:
            Image.Image: Image PIL du texte.
        """
        img = Image.new("RGB", (self.tile_width, self.tile_height), (0,0,0))
        draw = ImageDraw.Draw(img)
        font = ImageFont.load_default()
        draw.text((0,0), text, fill=color, font=font)
        return img

    def _render_image(self, img_path: str) -> Image.Image:
        """
        Ouvre une image et la redimensionne aux dimensions du panneau.

        Args:
            img_path (str): Chemin vers l'image.

        Returns:
            Image.Image: Image redimensionnée.
        """
        img = Image.open(img_path).convert("RGB")
        img = img.resize((self.tile_width, self.tile_height))
        return img

    async def send(self, payload: str | str, **kwargs) -> None:
        """
        Envoie un texte ou une image au panneau via BLE.

        Args:
            payload (str | str): Texte ou chemin d'image.
            **kwargs: Paramètres optionnels comme 'color' pour le texte.
        """
        if isinstance(payload, str) and payload.lower().endswith(('.png','.jpg','.jpeg')):
            img = self._render_image(payload)
        else:
            img = self._render_text(payload, color=kwargs.get("color", (255,255,255)))

        buf: bytes = img.tobytes()
        await self.transport.send(buf)
