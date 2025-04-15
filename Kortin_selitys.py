#Kortin selitys

import textwrap # Tämä kirjasto mahdollistaa tekstin muotoilun

def hae_kortin_selitys(tiedosto, kortin_numero):
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

    return "Korttia ei löytynyt."

def kortin_selitys():
    tiedosto = "elamankortit.txt"

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
    selitys = hae_kortin_selitys(tiedosto, kortin_numero)
   
    # Muotoillaan selitys siten, että se ei ylitä 70 merkkiä, näin selityksiä on vähän mukavampia lukea
    kappaleet = selitys.split("\n\n") # Oletetaan, että kappaleet on erotettu kahdella rivinvaihdolla
    muotoiltu_selitys = "\n\n".join([textwrap.fill(kappale, width=90) for kappale in kappaleet])
    
    print("\n" + muotoiltu_selitys + "\n")


kortin_selitys()