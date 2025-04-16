import time
import textwrap
import lukija
import random
from varit import RED, GREEN, LILA, BLUE, YELLOW, DEEPMAGENTA, PINK, ORANGE, RESET

def kortin_selitys():
    tiedosto = "isoarcana.txt"
    text = '☾ ⋆*･ﾟ:⋆*･ﾟ'

<<<<<<< HEAD
    kortit_lista = ['0. Narri,','1. Maagikko', '2. Ylipapitar', '3. Hallitsijatar', '4. Hallitsija', '5. Ylipappi',
                '6. Rakastavaiset', '7. Vaunut', '8. Voima', '9. Erakko', '10. Kohtalonpyörä', '11. Oikeus', '12. Hirtetty',
                '13. Kuolema', '14. Kohtuus', '15. Paholainen', '16. Torni', '17. Tähti', '18. Kuu', '19. Aurinko', '20. Tuomio', '21. Maailma']

    for kortti in kortit_lista:
        print(kortti)
=======
    kortit_lista = []

>>>>>>> f249566e31d346bef2a53e768eebd6aaf34f3262
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
            print(f"{RED}""\nAnna numero välillä 0-21, ei kirjainta tai muuta merkkiä."f"{RESET}")


    selitys = lukija.lue_tiedosto(tiedosto, kortin_numero)
   
    # Muotoillaan selitys siten, että se ei ylitä 90 merkkiä, näin selityksiä on vähän mukavampia lukea
    kappaleet = selitys.split("\n\n")
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