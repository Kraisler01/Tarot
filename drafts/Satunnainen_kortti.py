#Satunnainen kortti - Ennustus/Kysymys

import random
import time

RED = '\033[38;2;255;0;95m'
GREEN = '\033[38;2;135;215;135m'
LILA = '\033[38;2;215;175;225m'
BLUE = '\033[38;2;135;215;225m'
YELLOW = '\033[38;2;255;255;135m'
PINK = '\033[38;2;255;175;255m'
CYAN = '\033[96m'
RESET = '\033[0m'


def lue_tiedosto(tiedosto, kortin_numero):
    # Tämä funktio lukee tiedoston ja etsii kortin selityksen kortin numeron perusteella
    # UTF-8 koodi mahdollistaa erikoismerkkien käsittelyn kuten ääkköset
    try:
        with open(tiedosto, "r", encoding="utf-8") as f:
            sisältö = f.read()
    except FileNotFoundError:
        return "Tiedostoa ei löytynyt."

    # Oletetaan, että kortit on erotettu kolmella tyhjällä rivillä = "\n\n\n"
    kortit = sisältö.split("\n\n\n")

    # For loop käy läpi kaikki kortit ja etsii kortin numeron, välilyönnin ja väliviivan
    # perusteella oikean kortin selityksen
    for kortti in kortit:
        if kortti.startswith(f"{kortin_numero} –"): 
            return kortti

def satunnainen_kortti():
    print("\n" + "Kysy mielessäsi kysymys ja anna universumin vastata." + "\n")
    input("Paina Enter ja anna kortin johdattaa sinut vastauksen äärelle..." + "\n")

    # Tämä funktio valitsee satunnaisen kortin ja tulostaa sen selityksen
    kortin_numero = random.choice(range(1, 23))  #choice() valitsee satunnaisen kortin
    selitys = lue_tiedosto("ennustus.txt", kortin_numero)

    time.sleep(1)
    print("Sekoitetaan kortteja...\n")
    time.sleep(2)
    print(f"Nostit kortin:"f"{GREEN}""\n\n" + selitys + "\n"f"{RESET}")


satunnainen_kortti()