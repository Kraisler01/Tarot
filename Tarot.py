
def vuodenkortti():

    paiva = int(input("Anna syntymäpäivä (pp): "))
    kuukausi = int(input("Anna syntymäkuukausi(kk): "))
    vuosi = int(input("Anna syntymävuosi(vvvv): "))

    luku = paiva + kuukausi + vuosi

    while luku >= 4: # 4 on lukujen määrä
        luku = sum(int(luku) for luku in str(luku)) # muuttaa yhteenlasketun summan erillisiksi luvuiksi ja laskee yhteen
        print("Luku on:", luku)
        break
    

        

    
#def elamankortti():

#def vapaaa_kortti():
    #print("Sulje silmäsi, hengitä syvään ja tunne, mikä kortti kutsuu sinua.")


def main():
    

    print("Tervetuloa korttien viisauden äärelle - tässä tilassa universumi puhuu!")
    print("Valitse kortti:")
    print("1. Vuoden kortti")
    #print("2. Elämän kortti")
    #print("3. Vapaan kortti")
    print("4. Lopeta peli")

    valinta = input("Valintasi (1/2/3/4): ")

    if valinta == "1":
        vuodenkortti()
    #elif valinta == "2":
       # elamankortti()
    #elif valinta == "3":
    #    vapaaa_kortti()
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