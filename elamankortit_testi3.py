import textwrap
import time
import random

RED = '\033[38;2;255;0;95m'
GREEN = '\033[38;2;135;215;135m'
LILA = '\033[38;2;215;175;225m'
BLUE = '\033[38;2;135;215;225m'
YELLOW = '\033[38;2;255;255;135m'
DEEPMAGENTA = '\033[38;2;128;0;128m'
PINK = '\033[38;2;255;105;170m'
ORANGE = '\033[38;2;240;163;10m'
CYAN = '\033[96m'
RESET = '\033[0m'

def lue_tiedosto(tiedosto, kortti2):
    # Lukee tiedoston ja etsii selityksen kortin numeron perusteella
    # UTF-8 koodi mahdollistaa erikoismerkkien käsittelyn (kuten ääkköset)
    try:
        with open(tiedosto, "r", encoding="utf-8") as f:
            sisältö = f.read()
    except FileNotFoundError:
        return "Tiedostoa ei löytynyt."

    # Oletetaan, että kortit on erotettu kolmella rivinvaihdolla = "\n\n\n"
    kortit = sisältö.split("\n\n\n")

    # For loop käy läpi kaikki kortit ja etsii kortin numeron, välilyönnin ja väliviivan
    # perusteella oikean kortin selityksen
    for kortti in kortit:
        if kortti.startswith(f"{kortti2} –"):
            return kortti

def elaman_kortti():

    tiedosto = "elamankortit.txt"
    text = '☾ ⋆*･ﾟ:⋆*･ﾟ'

    try:
        paiva = int(input("Anna syntymäpäivä (pp): "))
        kuukausi = int(input("Anna syntymäkuukausi(kk): "))
        vuosi = int(input("Anna syntymävuosi(vvvv): "))

        vuoden_parit = [int(vuosi) for vuosi in str(vuosi)]
        kortti1 = (paiva + kuukausi + sum(vuoden_parit)) // 10 + (paiva + kuukausi + sum(vuoden_parit)) % 10
        kortti2 = ""
    except ValueError:
        print('Hups, en tunnista tätä päivämäärää. Syötäthän vain kokonaislukuja!')
        return
    
    if kortti1 == 10:
        kortti2 = 19
    elif kortti1 < 10:
        kortti2 = kortti1 + 9
    else:
        kortti2 = (kortti1 // 10) + (kortti1 % 10)

    print(f"{GREEN}Kortin numero on ensimmäisen laskun jälkeen: {kortti1}{RESET}")
    print(f"{GREEN}Kortin numero on toisen laskun jälkeen: {kortti2}{RESET}")
    
    if kortti2 < 10 or kortti2 > 22:    # Tarkistaa löytyykö lukua vastaavaa korttia
        print(f"{RED}Kortin numero ei vastaa kortteja pakassa.{RESET}")
        return
    
    selitys = lue_tiedosto(tiedosto, kortti2)
   
    if selitys is None:
        print(f"{RED}Kortin selitystä ei löytynyt tiedostosta.{RESET}")
        return

    kappaleet = selitys.split("\n\n")
    muotoiltu_selitys = "\n\n".join([textwrap.fill(kappale, width=90) for kappale in kappaleet])

    print("\nHaetaan korttia pakasta...\n")
    for char in text:
        print(f"{YELLOW}{char}{RESET}", end='', flush=True)
        time.sleep(0.3)

    print(f"{ORANGE}\n\n{muotoiltu_selitys}\n{RESET}")
    time.sleep(2)

elaman_kortti()