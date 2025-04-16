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



def elämänkortti():

    tiedosto = "elamankortit.txt"
    text = '☾ ⋆*･ﾟ:⋆*･ﾟ'

    paiva = int(input("Anna syntymäpäivä (pp): "))
    kuukausi = int(input("Anna syntymäkuukausi(kk): "))
    vuosi = int(input("Anna syntymävuosi(vvvv): "))

    vuoden_parit = [int(vuosi) for vuosi in str(vuosi)]
    kortin_numero = paiva + kuukausi + sum(vuoden_parit)

    print(f"{GREEN}Kortin numero on ensimmäisen laskun jälkeen: {kortin_numero}{RESET}")

    if 10 <= kortin_numero <= 99:
        kortin_numero = sum(int(kortin_numero) for kortin_numero in str(kortin_numero))

    print(f"{GREEN}Kortin numero on toisen laskun jälkeen: {kortin_numero}{RESET}")

    korttipakka = {10,11,12,13,14,15,16,17,18,19,20,21} # korttipakka 10-21
    
    if kortin_numero == 8:
        kortin_numero = 17

    elif kortin_numero == 19:
       kortin_numero =19 #maagikko 3 korttia, kortti 1,10,19
    
    elif kortin_numero == 10:
        kortin_numero = 10

    elif kortin_numero == 11:
        kortin_numero = 11
    
    elif kortin_numero == 20:
        kortin_numero =20

    elif kortin_numero == 12:
        kortin_numero = 12
    
    elif kortin_numero == 21: 
        kortin_numero = 21

    kortin_numero = korttipakka.get(kortin_numero, None)
    if kortin_numero is None:
        print(f"{RED}Kortin numero ei vastaa kortteja pakassa.{RESET}")
        return

    selitys = lue_tiedosto(tiedosto, kortin_numero)

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

elämänkortti()

