
import time
import laskettavat_kortit
import nosta_kortti
from varit import RED, GREEN, LILA, BLUE, YELLOW, DEEPMAGENTA, PINK, ORANGE, RESET

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

    # Tulostaa ohjeet

    print(f"{YELLOW}""\nTervetuloa korttien viisauden äärelle - tässä tilassa universumi puhuu!"f"{RESET}")
    print(f'''
    {LILA}Ohjeita käyttäjälle:{RESET}
          
        {ORANGE}1 – Vuoden kortti{RESET}
    {LILA}Nosta esiin vuoden matkan ydinenergia. Mitä oppia, valoa tai haastetta tämä vuosi tuo sinulle?{RESET}
    
        {PINK}2 – Elämän kortit{RESET}
    {LILA}Nämä kortit kulkevat kanssasi koko elämäsi – kuin sielun kompassi.{RESET}
    
        {GREEN}3 – Kysy korteilta{RESET}
    {LILA}Onko mielesi mutkalla? Nosta ohjaava kortti ja anna sen viestin valaista tiesi.{RESET}

        {BLUE}4 – Kortin selitys{RESET}
    {LILA}Haluatko ymmärtää tiettyä korttia syvemmin? Syötä kortin numero ja näät selityksen.{RESET}
        ''')
    
    # Palaa loopin avulla valikkoon kunnes käyttäjä valitsee lopettaa
    while True:
        time.sleep(1)
        nayta_valikko()
       
        try:
            
            valinta = input(f"{LILA}""Valintasi (0/1/2/3/4): "f"{RESET}")

            # Ohjaa käyttäjän valintarakenteen avulla oikeaan funktioon
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
                break
            else:
                print(f"{LILA}""\nJos haluat, voimme kokeilla uudelleen. Valitse intuitiosi avulla"f"{RESET}")

            # Kysyy ja käsittelee jatketaanko ohjelmaa
            print(f"{LILA}""\nKaipaavatko sydämesi ja mielesi vielä lisää opastusta korttien kautta?\n"f"{RESET}")
            another_one = input(f"{LILA}""Valinta on sinun (1 Kyllä /2 Ei): "f"{RESET}")

            if another_one == "1":
                continue
            if another_one == "2":
                print(f"{LILA}""\nIstuntomme päättyy, mutta korttien taika jää kanssasi. Pidä huolta itsestäsi!\n"f"{RESET}")
                break
            else:
                print(f"{LILA}""\nValinta ei ole oikein, mutta voit aina palata korttien pariin. Kiitos ja näkemiin!\n"f"{RESET}")
                break

        # Ottaa kiinni muualla käsittelemättömät yleisimmät virheet, tallentaa tiedot muuttujaan ja tulostaa ne käyttäjälle
        except Exception as e:
            print(f"Tapahtui virhe: {e}.")
main()