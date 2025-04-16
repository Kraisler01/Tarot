
def lue_tiedosto(tiedosto, kortin_numero):

    # Funktio lukee tiedoston ja etsii kortin selityksen numeron perusteella
    # UTF-8 koodi mahdollistaa erikoismerkkien käsittelyn kuten ääkköset

    try:
        with open(tiedosto, "r", encoding="utf-8") as f:
            sisältö = f.read()
    except FileNotFoundError:
        return "Tiedostoa ei löytynyt."

    kortit = sisältö.split("\n\n\n")

    # Käy läpi kaikki kortit ja etsii oikean selityksen
    for kortti in kortit:
        if kortti.startswith(f"{kortin_numero} –"): 
            return kortti
        