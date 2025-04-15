
import time
import laskettavat_kortit
import nosta_kortti

#Määritellään RGB-värikoodit vakioina:

RED = '\033[38;2;255;0;95m'
GREEN = '\033[38;2;135;215;135m'
LILA = '\033[38;2;215;175;225m'
BLUE = '\033[38;2;135;215;225m'
YELLOW = '\033[38;2;255;255;135m'
DEEPMAGENTA = '\033[38;2;128;0;128m'
PINK = '\033[38;2;255;105;170m'
ORANGE = '\033[38;2;255;160;122m'
CYAN = '\033[96m'
RESET = '\033[0m'

# def lue_tiedosto(tiedosto, kortin_numero):
#     # Tämä funktio lukee tiedoston ja etsii kortin selityksen kortin numeron perusteella
#     # UTF-8 koodi mahdollistaa erikoismerkkien käsittelyn kuten ääkköset
#     try:
#         with open(tiedosto, "r", encoding="utf-8") as f:
#             sisältö = f.read()
#     except FileNotFoundError:
#         return "Tiedostoa ei löytynyt."

#     # Oletetaan, että kortit on erotettu kolmella tyhjällä rivillä = "\n\n\n"
#     kortit = sisältö.split("\n\n\n")

#     # For loop käy läpi kaikki kortit ja etsii kortin numeron, välilyönnin ja väliviivan
#     # perusteella oikean kortin selityksen
#     for kortti in kortit:
#         if kortti.startswith(f"{kortin_numero} –"): 
#             return kortti

def nayta_valikko():
    print(f'''
        Syötä haluamaasi toimenpidettä vastaava luku.

        {ORANGE}1 Vuoden kortti{RESET}
        {PINK}2 Elämän kortti{RESET}
        {GREEN}3 Kysy korteilta{RESET}
        {BLUE}4 Hae kortin selitys{RESET}
        {DEEPMAGENTA}0 Lopeta ohjelma{RESET}
        ''')

# def vuodenkortti():
#     tiedosto = "vuodenkortti.txt"
#     text = '☾ ⋆*･ﾟ:⋆*･ﾟ'

#     while True:
#         try:
#             paiva = int(input("\nAnna syntymäpäivä (pp): "))
#             if not 1 <= paiva <= 31:
#                 raise ValueError
#             break
#         except ValueError:
#             print(f"{RED}""\nSyötä kelvollinen päivä (1–31)."f"{RESET}")

#     while True:
#         try:
#             kuukausi = int(input("Anna syntymäkuukausi (kk): "))
#             if not 1 <= kuukausi <= 12:
#                 raise ValueError
#             break
#         except ValueError:
#             print(f"{RED}""\nSyötä kelvollinen kuukausi (1–12)."f"{RESET}")

#     while True:
#         try:
#             vuosi = int(input("Anna vuosi, jolle haluat nostaa kortin esim. 2025 (vvvv): "))
#             if not 1000 <= vuosi <= 9999:
#                 raise ValueError
#             break
#         except ValueError:
#             print(f"{RED}""\nSyötä kelvollinen vuosiluku nelinumeroisena (esim. 2025)."f"{RESET}")

#     luku = paiva + kuukausi + vuosi

#     while luku >= 22:  
#         luku = sum(int(numero) for numero in str(luku))  

#     selitys = lukija.lue_tiedosto(tiedosto, luku)
   
#     # Muotoillaan selitys siten, että se ei ylitä 90 merkkiä, näin selityksiä on vähän mukavampia lukea
#     kappaleet = selitys.split("\n\n") # Oletetaan, että kappaleet on erotettu kahdella rivinvaihdolla
#     muotoiltu_selitys = "\n\n".join([textwrap.fill(kappale, width=90) for kappale in kappaleet])
    
#     print("\nHaetaan korttia pakasta...\n")
#     for char in text:
#         print(f"{YELLOW}{char}{RESET}", end='', flush=True)
#         time.sleep(0.3)
    
#     print(f"{ORANGE}""\n\n" + muotoiltu_selitys + "\n"f"{RESET}")
#     time.sleep(2)

# def elaman_kortti():

#     tiedosto = "elamankortit.txt"
#     text = '☾ ⋆*･ﾟ:⋆*･ﾟ'

#     try:
#         paiva = int(input("Anna syntymäpäivä (pp): "))
#         kuukausi = int(input("Anna syntymäkuukausi(kk): "))
#         vuosi = int(input("Anna syntymävuosi(vvvv): "))

#         vuoden_parit = [int(vuosi) for vuosi in str(vuosi)]
#         kortti1 = (paiva + kuukausi + sum(vuoden_parit)) // 10 + (paiva + kuukausi + sum(vuoden_parit)) % 10
#         kortti2 = ""
#     except ValueError:
#         print('Hups, en tunnista tätä päivämäärää. Syötäthän vain kokonaislukuja!')
#         return
    
#     if kortti1 == 10:
#         kortti2 = 19
#     elif kortti1 < 10:
#         kortti2 = kortti1 + 9
#     else:
#         kortti2 = (kortti1 // 10) + (kortti1 % 10)

#     print(f"{GREEN}Kortin numero on ensimmäisen laskun jälkeen: {kortti1}{RESET}")
#     print(f"{GREEN}Kortin numero on toisen laskun jälkeen: {kortti2}{RESET}")
    
#     if kortti2 < 10 or kortti2 > 22:    # Tarkistaa löytyykö lukua vastaavaa korttia
#         print(f"{RED}Kortin numero ei vastaa kortteja pakassa.{RESET}")
#         return
    
#     selitys = lukija.lue_tiedosto(tiedosto, kortti2)
   
#     if selitys is None:
#         print(f"{RED}Kortin selitystä ei löytynyt tiedostosta.{RESET}")
#         return

#     kappaleet = selitys.split("\n\n")
#     muotoiltu_selitys = "\n\n".join([textwrap.fill(kappale, width=90) for kappale in kappaleet])

#     print("\nHaetaan korttia pakasta...\n")
#     for char in text:
#         print(f"{YELLOW}{char}{RESET}", end='', flush=True)
#         time.sleep(0.3)

#     print(f"{ORANGE}\n\n{muotoiltu_selitys}\n{RESET}")
#     time.sleep(2)

# def satunnainen_kortti():
#     text = "*✧･ﾟ: *✧･ﾟ:"

#     print("\n" + "Kysy mielessäsi kysymys ja anna universumin vastata." + "\n")
#     input("Paina Enter ja anna kortin johdattaa sinut vastauksen äärelle..." + "\n")

#     # Tämä funktio valitsee satunnaisen kortin ja tulostaa sen selityksen
#     kortin_numero = random.choice(range(1, 23))  #choice() valitsee satunnaisen kortin
#     selitys = lukija.lue_tiedosto("ennustus.txt", kortin_numero)

#     time.sleep(1)
#     print("Sekoitetaan kortteja...\n")
    
#     # Tulosta jokainen merkki puolen sekunnin välein
#     for char in text:
#         print(f"{YELLOW}{char}{RESET}", end='', flush=True)
#         time.sleep(0.3)
    
#     print(f"\n\nNostit kortin:"f"{GREEN}""\n\n" + selitys + "\n"f"{RESET}")


# def kortin_selitys():
#     tiedosto = "isoarcana.txt"
#     text = '☾ ⋆*･ﾟ:⋆*･ﾟ'

#     #Tehdään looppi, joka pyytää käyttäjältä kortin numeroa
#     #ja tarkistaa, että se on oikea
#     while True: 
#         try:
#             kortin_numero = int(input("\nAnna kortin numero, josta haluat tietää lisää (0–21): "))
#             if 0 <= kortin_numero <= 21:
#                 break  # Jos syöte on kelvollinen, poistutaan loopista
#             else:
#                 print(f"{RED}""\nKortin numeron tulee olla välillä 0–21."f"{RESET}")
#         except ValueError:
#             print(f"{RED}""Anna numero välillä 0-21, ei kirjainta tai muuta merkkiä."f"{RESET}")

#     #Haetaan kortin selitys funktiosta, joka lukee sisältöä tiedostosta
#     #ja etsii kortin numeron perusteella selityksen
#     selitys = lukija.lue_tiedosto(tiedosto, kortin_numero)
   
#     # Muotoillaan selitys siten, että se ei ylitä 90 merkkiä, näin selityksiä on vähän mukavampia lukea
#     kappaleet = selitys.split("\n\n") # Oletetaan, että kappaleet on erotettu kahdella rivinvaihdolla
#     muotoiltu_selitys = "\n\n".join([textwrap.fill(kappale, width=90) for kappale in kappaleet])
    
#     print("\nHaetaan korttia pakasta...\n")
#     for char in text:
#         print(f"{YELLOW}{char}{RESET}", end='', flush=True)
#         time.sleep(0.3)
    
#     print(f"{BLUE}""\n\n" + muotoiltu_selitys + "\n"f"{RESET}")
#     time.sleep(2)


def main():
    print(f"{LILA}""\nTervetuloa korttien viisauden äärelle - tässä tilassa universumi puhuu!"f"{RESET}")
    time.sleep(1)
    nayta_valikko()

    valinta = input(f"{LILA}""Valintasi (0/1/2/3/4): "f"{RESET}")

    if valinta == "1":
        laskettavat_kortit.vuodenkortti()
    elif valinta == "2":
        laskettavat_kortit.elaman_kortti()
    elif valinta == "3":
        nosta_kortti.satunnainen_kortti()
    elif valinta == "4":
        nosta_kortti.kortin_selitys()
    elif valinta == "0":
        print(f"{YELLOW}""\n*✧･ﾟ: *✧･ﾟKiitos ja näkemiin! ☾ ⋆*･ﾟ:⋆*･ﾟ\n"f"{RESET}")
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