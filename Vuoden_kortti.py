#Vuoden kortti

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

#En saanut tätä toimimaan? :--()

# def vuodenkortti():
#     tiedosto = "vuodenkortti.txt"

#     paiva = int(input("Anna syntymäpäivä (pp): "))
#     kuukausi = int(input("Anna syntymäkuukausi(kk): "))
#     vuosi = int(input("Anna syntymävuosi(vvvv): "))

#     luku = paiva + kuukausi + vuosi

#     while luku >= 4: # 4 on numeroiden määrä
#         luku = sum(int(luku) for luku in str(luku)) # muuttaa yhteenlasketun summan erillisiksi luvuiksi ja laskee yhteen
    
    
#     print(f"Vuoden korttisi on: {luku}")
#     selitys = lue_tiedosto(tiedosto, luku)
#     print(f"Nostit kortin:\n\n" + selitys + "\n")
#     return selitys

# vuodenkortti()

def vuodenkortti():
    tiedosto = "vuodenkortti.txt"

    paiva = int(input("Anna syntymäpäivä (pp): "))
    kuukausi = int(input("Anna syntymäkuukausi(kk): "))
    vuosi = int(input("Anna syntymävuosi(vvvv): "))

    luku = paiva + kuukausi + vuosi

    while luku >= 10:
        luku = sum(int(digit) for digit in str(luku))  

    print(f"\nVuoden korttisi on: {luku}")
    selitys = lue_tiedosto(tiedosto, luku)
    print(f"\n\n" + selitys + "\n")
    return selitys

vuodenkortti()


