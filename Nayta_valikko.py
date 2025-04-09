def nayta_valikko():

    print("\n--- Tarot-ohjelma ---")
    print("\n1. Vuoden kortti")
    print("2. Elämän kortti")
    print("3. Kysy korteilta")
    print("4. Hae kortin selitys")
    print("0. Lopeta")




def main():
    print("Tervetuloa korttien viisauden äärelle - tässä tilassa universumi puhuu!")
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