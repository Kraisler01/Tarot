import time
import textwrap
import lukija
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
    selitys = lukija.lue_tiedosto(tiedosto, kortin_numero)
   
    # Muotoillaan selitys siten, että se ei ylitä 90 merkkiä, näin selityksiä on vähän mukavampia lukea
    kappaleet = selitys.split("\n\n") # Oletetaan, että kappaleet on erotettu kahdella rivinvaihdolla
    muotoiltu_selitys = "\n\n".join([textwrap.fill(kappale, width=90) for kappale in kappaleet])
    
    print("\nHaetaan korttia pakasta...\n")
    for char in text:
        print(f"{YELLOW}{char}{RESET}", end='', flush=True)
        time.sleep(0.3)
    
    print(f"{BLUE}""\n\n" + muotoiltu_selitys + "\n"f"{RESET}")
    time.sleep(2)


def satunnainen_kortti():
    text = "*✧･ﾟ: *✧･ﾟ:"

    print("\n" + "Kysy mielessäsi kysymys ja anna universumin vastata." + "\n")
    input("Paina Enter ja anna kortin johdattaa sinut vastauksen äärelle..." + "\n")

    # Tämä funktio valitsee satunnaisen kortin ja tulostaa sen selityksen
    kortin_numero = random.choice(range(1, 23))  #choice() valitsee satunnaisen kortin
    selitys = lukija.lue_tiedosto("ennustus.txt", kortin_numero)

    time.sleep(1)
    print("Sekoitetaan kortteja...\n")
    
    # Tulosta jokainen merkki puolen sekunnin välein
    for char in text:
        print(f"{YELLOW}{char}{RESET}", end='', flush=True)
        time.sleep(0.3)
    
    print(f"\n\nNostit kortin:"f"{GREEN}""\n\n" + selitys + "\n"f"{RESET}")