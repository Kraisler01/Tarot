import time
import lukija
import textwrap
from varit import RED, GREEN, LILA, BLUE, YELLOW, DEEPMAGENTA, PINK, ORANGE, RESET

def elaman_kortti():
    tiedosto = "elamankortit.txt"
    text = '☾ ⋆*･ﾟ:⋆*･ﾟ'

    # Toistorakenne käsittelee päivän, kuukauden ja vuoden syötteet erikseen, tarkistaa päivämäärien oikeellisuuden
    # ja pyytää syötteen tarvittaessa uudelleen ennen kuin siirtyy seuraavaan. 

    while True:
        try:
            paiva = int(input("\nAnna syntymäpäivä (pp): "))
            if not 1 <= paiva <= 31:
                raise ValueError
            break
        except ValueError:
            print(f"{RED}""\nSyötä kelvollinen päivä (1–31)."f"{RESET}")

    while True:
        try:
            kuukausi = int(input("\nAnna syntymäkuukausi (kk): "))
            if not 1 <= kuukausi <= 12:
                raise ValueError
            break
        except ValueError:
            print(f"{RED}""\nSyötä kelvollinen kuukausi (1–12)."f"{RESET}")

    while True:
        try:
            vuosi = int(input("\nAnna syntymävuosi (vvvv): "))
            if not 1000 <= vuosi <= 9999:
                raise ValueError
            break
        except ValueError:
            print(f"{RED}""\nSyötä kelvollinen vuosiluku nelinumeroisena (esim. 2025)."f"{RESET}")

    # Erottelee vuosiluvun yksittäisiksi numeroiksi ja laskee kortin 1
    vuoden_parit = [int(vuosi) for vuosi in str(vuosi)]
    kortti1 = (paiva + kuukausi + sum(vuoden_parit)) // 10 + (paiva + kuukausi + sum(vuoden_parit)) % 10
    kortti2 = ""

    # Poikkeustapaukset 2. kortin laskukaavassa ja pääasiallinen laskukaava
    if kortti1 == 10:
        kortti2 = 19
    elif kortti1 < 10:
        kortti2 = kortti1 + 9
    else:
        kortti2 = (kortti1 // 10) + (kortti1 % 10)
        
    # Poikkeus 2. kortin laskukaavassa
    if kortti2 < 10:
        kortti2 = kortti1

    # Tarkistaa, löytyykö lukua vastaavaa korttia
    if kortti2 < 10 or kortti2 > 22:
        print(f"{RED}Kortin numero ei vastaa kortteja pakassa.{RESET}")
        return
    
    selitys = lukija.lue_tiedosto(tiedosto, kortti2)

    # Tarkistaa, löytyykö selitytä tiedostosta
    if selitys is None:
        print(f"{RED}Kortin selitystä ei löytynyt tiedostosta.{RESET}")
        return

    # Hakee ja muotoilee selityksen helpommin luettavaksi
    kappaleet = selitys.split("\n\n")
    muotoiltu_selitys = "\n\n".join([textwrap.fill(kappale, width=90) for kappale in kappaleet])

    print("\nHaetaan korttia pakasta...\n")
    for char in text:
        print(f"{YELLOW}{char}{RESET}", end='', flush=True)
        time.sleep(0.3)

    print(f"{PINK}\n\n{muotoiltu_selitys}\n{RESET}")
    time.sleep(2)




def vuodenkortti():
    tiedosto = "vuodenkortti.txt"
    text = '☾ ⋆*･ﾟ:⋆*･ﾟ'

    # Toistorakenne käsittelee päivän, kuukauden ja vuoden syötteet erikseen, tarkistaa päivämäärien oikeellisuuden
    # ja pyytää syötteen tarvittaessa uudelleen ennen kuin siirtyy seuraavaan. 

    while True:
        try:
            paiva = int(input("\nAnna syntymäpäivä (pp): "))
            if not 1 <= paiva <= 31:
                raise ValueError
            break
        except ValueError:
            print(f"{RED}""\nSyötä kelvollinen päivä (1–31)."f"{RESET}")

    while True:
        try:
            kuukausi = int(input("Anna syntymäkuukausi (kk): "))
            if not 1 <= kuukausi <= 12:
                raise ValueError
            break
        except ValueError:
            print(f"{RED}""\nSyötä kelvollinen kuukausi (1–12)."f"{RESET}")

    while True:
        try:
            vuosi = int(input("Anna vuosi, jolle haluat nostaa kortin esim. 2025 (vvvv): "))
            if not 1000 <= vuosi <= 9999:
                raise ValueError
            break
        except ValueError:
            print(f"{RED}""\nSyötä kelvollinen vuosiluku nelinumeroisena (esim. 2025)."f"{RESET}")


    luku = paiva + kuukausi + vuosi

    # Laskee luvun jokaisen numeron yksitellen yhteen
    while luku >= 22:  
        luku = sum(int(numero) for numero in str(luku))  

    selitys = lukija.lue_tiedosto(tiedosto, luku)
   
    # Muotoillaan selitys siten, että se ei ylitä 90 merkkiä
    kappaleet = selitys.split("\n\n")
    muotoiltu_selitys = "\n\n".join([textwrap.fill(kappale, width=90) for kappale in kappaleet])
    
    print("\nHaetaan korttia pakasta...\n")
    for char in text:
        print(f"{YELLOW}{char}{RESET}", end='', flush=True)
        time.sleep(0.3)
    
    print(f"{ORANGE}""\n\n" + muotoiltu_selitys + "\n"f"{RESET}")
    time.sleep(2)