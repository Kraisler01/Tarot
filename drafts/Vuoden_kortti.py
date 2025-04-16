#Vuoden kortti
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
        


def vuodenkortti():
    tiedosto = "vuodenkortti.txt"
    text = '☾ ⋆*･ﾟ:⋆*･ﾟ'

    while True:
        try:
            paiva = int(input("\nAnna syntymäpäivä (pp): "))
            if not 1 <= paiva <= 31:
                raise ValueError
            break
        except ValueError:
            print("Syötä kelvollinen päivä (1–31).")

    while True:
        try:
            kuukausi = int(input("Anna syntymäkuukausi (kk): "))
            if not 1 <= kuukausi <= 12:
                raise ValueError
            break
        except ValueError:
            print("Syötä kelvollinen kuukausi (1–12).")

    while True:
        try:
            vuosi = int(input("Anna vuosi, jolle haluat nostaa kortin esim. 2025 (vvvv): "))
            if not 1000 <= vuosi <= 9999:
                raise ValueError
            break
        except ValueError:
            print("Syötä kelvollinen vuosiluku nelinumeroisena (esim. 2025).")

    luku = paiva + kuukausi + vuosi

    while luku >= 22:  
        luku = sum(int(numero) for numero in str(luku))  

    selitys = lue_tiedosto(tiedosto, luku)
   
    # Muotoillaan selitys siten, että se ei ylitä 90 merkkiä, näin selityksiä on vähän mukavampia lukea
    kappaleet = selitys.split("\n\n") # Oletetaan, että kappaleet on erotettu kahdella rivinvaihdolla
    muotoiltu_selitys = "\n\n".join([textwrap.fill(kappale, width=90) for kappale in kappaleet])
    
    print("\nHaetaan korttia pakasta...\n")
    for char in text:
        print(f"{YELLOW}{char}{RESET}", end='', flush=True)
        time.sleep(0.3)
    
    print(f"{ORANGE}""\n\n" + muotoiltu_selitys + "\n"f"{RESET}")
    time.sleep(2)

vuodenkortti()


