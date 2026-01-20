from PIL import Image, ImageDraw, ImageFont
from typing import Tuple

def render_text(text: str, width: int, height: int, color: Tuple[int,int,int] = (255,255,255)) -> Image.Image:
    """
    Rend du texte dans une image RGB.

    Args:
        text (str): Texte à rendre.
        width (int): Largeur de l'image.
        height (int): Hauteur de l'image.
        color (Tuple[int,int,int], optional): Couleur du texte. Defaults to blanc.

    Returns:
        Image.Image: Image contenant le texte.
    """
    img = Image.new("RGB", (width, height), (0,0,0))
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    draw.text((0,0), text, fill=color, font=font)
    return img

def render_image(path: str, width: int, height: int) -> Image.Image:
    """
    Charge une image depuis un fichier et la redimensionne.

    Args:
        path (str): Chemin de l'image.
        width (int): Largeur cible.
        height (int): Hauteur cible.

    Returns:
        Image.Image: Image redimensionnée.
    """
    img = Image.open(path).convert("RGB")
    img = img.resize((width, height))
    return img
