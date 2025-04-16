
import time
import laskettavat_kortit
import nosta_kortti
from varit import RED, GREEN, LILA, BLUE, YELLOW, DEEPMAGENTA, PINK, ORANGE, CYAN, RESET


def nayta_valikko():
    print(f'''
        Syötä haluamaasi toimenpidettä vastaava luku.

        {ORANGE}1 Vuoden kortti{RESET}
        {PINK}2 Elämän kortti{RESET}
        {GREEN}3 Kysy korteilta{RESET}
        {BLUE}4 Hae kortin selitys{RESET}
        {DEEPMAGENTA}0 Lopeta ohjelma{RESET}
        ''')


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