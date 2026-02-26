# BkLightToolkit

![Build Status](https://img.shields.io/github/actions/workflow/status/LaArbre/BkLightToolkit/python-package.yml?branch=main)
![PyPI](https://img.shields.io/pypi/v/BkLightToolkit) bientôt :)

API Python pour piloter une matrice RGB 32×32 BK‑Light ACT1026 par Bluetooth Low Energy (BLE).
Inspiré par Bk‑Light‑AppBypass de Puparia (crédit), avec des adaptations originales et des extensions d’usage. ([GitHub Repo](https://github.com/LaArbre/BkLightToolkit))

## Table des matières

1. [Présentation](#présentation)
2. [Fonctionnalités](#fonctionnalités)
5. [Exemples de scripts](#example)
3. [Installation](#installation)
8. [Licence](#licence)

## Présentation

BkLightToolkit est un ensemble d’outils Python permettant de communiquer avec un panneau LED BK‑Light ACT1026 32×32 via BLE en utilisant la séquence de commandes extraite des logs fournis. D’autres panneaux peuvent fonctionner mais ne sont pas officiellement supportés.

## Fonctionnalités

- Connexion BLE transparente à la matrice LED.
- Envoi d’images, textes et animations.
- Gestion des paramètres LED (rotation, luminosité).
- Outils de tests automatiques (scripts unitaires).
- Possibilité de créer de nouveaux effets visuels.
- Interface CLI en cours de développement.

## Example
A venir

## Installation

Pré‑requis système

- Python 3.10+
- Bluetooth LE (adaptateur compatible BLE) installé et activé.

Installation du package

```bash
git clone https://github.com/LaArbre/BkLightToolkit.git
cd BkLightToolkit
pip install -r requirements.txt
```

## Licence

Licece MIT, voir fichier LICENCE
