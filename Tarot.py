import random
import textwrap
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

def nayta_valikko():

    print('''
    Syötä haluamaasi toimenpidettä vastaava luku.
        
    1 Vuoden kortti
    2 Elämän kortti
    3 Kysy korteilta
    4 Hae kortin selitys
    0 Lopeta ohjelma
    ''')


def satunnainen_kortti():
    
    text = "*✧･ﾟ: *✧･ﾟ:"

    print("\n" + "Kysy mielessäsi kysymys ja anna universumin vastata." + "\n")
    input("Paina Enter ja anna kortin johdattaa sinut vastauksen äärelle..." + "\n")

    # Tämä funktio valitsee satunnaisen kortin ja tulostaa sen selityksen
    kortin_numero = random.choice(range(1, 23))  #choice() valitsee satunnaisen kortin
    selitys = lue_tiedosto("ennustus.txt", kortin_numero)

    time.sleep(1)
    print("Sekoitetaan kortteja...\n")
    
    # Tulosta jokainen merkki puolen sekunnin välein
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.5)
    
    print(f"\n\nNostit kortin:"f"{GREEN}""\n\n" + selitys + "\n"f"{RESET}")


def kortin_selitys():
    tiedosto = "isoarcana.txt"
    text = '☾ ⋆*･ﾟ:⋆*･ﾟ'

    #Tehdään looppi, joka pyytää käyttäjältä kortin numeroa
    #ja tarkistaa, että se on oikea
    while True: 
        try:
            kortin_numero = int(input("\nAnna kortin numero, josta haluat tietää lisää (0–21): "))
            if 0 <= kortin_numero <= 21:
                break  # Jos syöte on kelvollinen, poistutaan loopista
            else:
                print(f"{RED}""\nKortin numeron tulee olla välillä 0–21."f"{RESET}")
        except ValueError:
            print(f"{RED}""Anna numero välillä 0-21, ei kirjainta tai muuta merkkiä."f"{RESET}")

    #Haetaan kortin selitys funktiosta, joka lukee sisältöä tiedostosta
    #ja etsii kortin numeron perusteella selityksen
    selitys = lue_tiedosto(tiedosto, kortin_numero)
   
    # Muotoillaan selitys siten, että se ei ylitä 90 merkkiä, näin selityksiä on vähän mukavampia lukea
    kappaleet = selitys.split("\n\n") # Oletetaan, että kappaleet on erotettu kahdella rivinvaihdolla
    muotoiltu_selitys = "\n\n".join([textwrap.fill(kappale, width=90) for kappale in kappaleet])
    
    print("\nHaetaan korttia pakasta...\n")
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.5)
    print(f"{BLUE}""\n\n" + muotoiltu_selitys + "\n"f"{RESET}")
    time.sleep(2)


def main():
    print(f"{LILA}""\nTervetuloa korttien viisauden äärelle - tässä tilassa universumi puhuu!"f"{RESET}")
    time.sleep(1)
    nayta_valikko()

    valinta = input(f"{LILA}""Valintasi (0/1/2/3/4): "f"{RESET}")

    if valinta == "1":
        vuoden_kortti()
    elif valinta == "2":
        elaman_kortti()
    elif valinta == "3":
        satunnainen_kortti()
    elif valinta == "4":
        kortin_selitys()
    elif valinta == "0":
        print(f"{PINK}""\n*✧･ﾟ: *✧･ﾟKiitos ja näkemiin! ☾ ⋆*･ﾟ:⋆*･ﾟ\n"f"{RESET}")
        return
    else:
        print(f"{LILA}""\nJos haluat, voimme kokeilla uudelleen. Valitse intuitiosi avulla"f"{RESET}")

    print(f"{LILA}""\nKaipaavatko sydämesi ja mielesi vielä lisää opastusta korttien kautta?\n"f"{RESET}")
    another_one = input(f"{LILA}""Valinta on sinun (1 Kyllä /2 Ei): "f"{RESET}")
    if another_one == "1":
        main()
    elif another_one == "2":
        print(f"{LILA}""\nIstuntomme päättyy, mutta korttien taika jää kanssasi. Pidä huolta itsestäsi!\n"f"{RESET}")
    else:
        print(f"{LILA}""\nValinta ei ole oikein, mutta voit aina palata korttien pariin. Kiitos ja näkemiin!\n"f"{RESET}")
main()

    
#def elamankortti():

