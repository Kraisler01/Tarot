import random
import textwrap


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
    print("\n" + "Kysy mielessäsi kysymys ja anna universumin vastata." + "\n")
    input("Paina Enter ja anna kortin johdattaa sinut vastauksen äärelle..." + "\n")

    # Tämä funktio valitsee satunnaisen kortin ja tulostaa sen selityksen
    kortin_numero = random.choice(range(1, 23))  #choice() valitsee satunnaisen kortin
    selitys = lue_tiedosto("ennustus.txt", kortin_numero)

    print(f"Nostit kortin:""\n\n" + selitys + "\n")


def kortin_selitys():
    tiedosto = "isoarcana.txt"

    #Tehdään looppi, joka pyytää käyttäjältä kortin numeroa
    #ja tarkistaa, että se on oikea
    while True: 
        try:
            kortin_numero = int(input("Anna kortin numero 0–21: "))
            if 0 <= kortin_numero <= 21:
                break  # Jos syöte on kelvollinen, poistutaan loopista
            else:
                print("Kortin numeron tulee olla välillä 0–21.")
        except ValueError:
            print("Anna numero välillä 0-21, ei kirjainta tai muuta merkkiä.")

    #Haetaan kortin selitys funktiosta, joka lukee sisältöä tiedostosta
    #ja etsii kortin numeron perusteella selityksen
    selitys = lue_tiedosto(tiedosto, kortin_numero)
   
    # Muotoillaan selitys siten, että se ei ylitä 90 merkkiä, näin selityksiä on vähän mukavampia lukea
    kappaleet = selitys.split("\n\n") # Oletetaan, että kappaleet on erotettu kahdella rivinvaihdolla
    muotoiltu_selitys = "\n\n".join([textwrap.fill(kappale, width=90) for kappale in kappaleet])
    
    print("\n" + muotoiltu_selitys + "\n")


def main():
    print("\nTervetuloa korttien viisauden äärelle - tässä tilassa universumi puhuu!")
    nayta_valikko()

    valinta = input("Valintasi (0/1/2/3/4): ")

    if valinta == "1":
        vuoden_kortti()
    elif valinta == "2":
        elaman_kortti()
    elif valinta == "3":
        satunnainen_kortti()
    elif valinta == "4":
        kortin_selitys()
    else:
        print("Jos haluat, voimme kokeilla uudelleen. Valitse intuitiosi avulla")

    print("Kaipaavatko sydämesi ja mielesi vielä lisää opastusta korttien kautta?? (1 Kyllä /2 Ei)")
    another_one = input("Valinta on sinun (1 Kyllä /2 Ei): ")
    if another_one == "1":
        main()
    elif another_one == "2":
        print("Istuntomme päättyy, mutta korttien taika jää kanssasi. Pidä huolta itsestäsi!")
    else:
        print("Valinta ei ole oikein, mutta voit aina palata korttien pariin. Kiitos ja näkemiin!")
main()

    
#def elamankortti():

#def vapaaa_kortti():
    #print("Sulje silmäsi, hengitä syvään ja tunne, mikä kortti kutsuu sinua.")
