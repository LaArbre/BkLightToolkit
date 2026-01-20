import asyncio
from typing import List, Any
from .panel import Panel

class PanelManager:
    """
    Gère un ensemble de panneaux et permet l'envoi de données
    en mode asynchrone ou synchrone.
    """
    def __init__(self, panels: List[Panel]) -> None:
        """
        Initialise le PanelManager avec une liste de panneaux.

        Args:
            panels (List[Panel]): Liste d'objets Panel à gérer.
        """
        self.panels = panels

    async def send(self, payload: Any, **kwargs) -> None:
        """
        Envoie des données à tous les panneaux de manière asynchrone.

        Args:
            payload (Any): Texte ou chemin d'image à envoyer.
            **kwargs: Paramètres optionnels comme 'color'.
        """
        tasks = [panel.send(payload, **kwargs) for panel in self.panels]
        await asyncio.gather(*tasks)

    def send_sync(self, payload: Any, **kwargs) -> None:
        """
        Envoie des données à tous les panneaux de manière synchrone.
        Utilise asyncio.run pour exécuter la coroutine.

        Args:
            payload (Any): Texte ou chemin d'image à envoyer.
            **kwargs: Paramètres optionnels comme 'color'.
        """
        asyncio.run(self.send(payload, **kwargs))
