import time
import lukija
import textwrap
from varit import RED, GREEN, LILA, BLUE, YELLOW, DEEPMAGENTA, PINK, ORANGE, CYAN, RESET

def elaman_kortti():

    tiedosto = "elamankortit.txt"
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
    # try:
    #     paiva = int(input("Anna syntymäpäivä (pp): "))
    #     kuukausi = int(input("Anna syntymäkuukausi(kk): "))
    #     vuosi = int(input("Anna syntymävuosi(vvvv): "))

    vuoden_parit = [int(vuosi) for vuosi in str(vuosi)]
    kortti1 = (paiva + kuukausi + sum(vuoden_parit)) // 10 + (paiva + kuukausi + sum(vuoden_parit)) % 10
    kortti2 = ""
        # except ValueError:
        # print('Hups, en tunnista tätä päivämäärää. Syötäthän vain kokonaislukuja!')
        # return

    if kortti1 == 10:
        kortti2 = 19
    elif kortti1 < 10:
        kortti2 = kortti1 + 9
    else:
        kortti2 = (kortti1 // 10) + (kortti1 % 10)
        
    if kortti2 < 10:
        kortti2 = kortti1

    if kortti2 < 10 or kortti2 > 22:    # Tarkistaa löytyykö lukua vastaavaa korttia
        print(f"{RED}Kortin numero ei vastaa kortteja pakassa.{RESET}")
        return
    
    selitys = lukija.lue_tiedosto(tiedosto, kortti2)
   
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

    while luku >= 22:  
        luku = sum(int(numero) for numero in str(luku))  

    selitys = lukija.lue_tiedosto(tiedosto, luku)
   
    # Muotoillaan selitys siten, että se ei ylitä 90 merkkiä, näin selityksiä on vähän mukavampia lukea
    kappaleet = selitys.split("\n\n") # Oletetaan, että kappaleet on erotettu kahdella rivinvaihdolla
    muotoiltu_selitys = "\n\n".join([textwrap.fill(kappale, width=90) for kappale in kappaleet])
    
    print("\nHaetaan korttia pakasta...\n")
    for char in text:
        print(f"{YELLOW}{char}{RESET}", end='', flush=True)
        time.sleep(0.3)
    
    print(f"{ORANGE}""\n\n" + muotoiltu_selitys + "\n"f"{RESET}")
    time.sleep(2)