def elämänkortti(tiedosto, kortin_numero):

    paiva = int(input("Anna syntymäpäivä (pp): "))
    kuukausi = int(input("Anna syntymäkuukausi(kk): "))
    vuosi = int(input("Anna syntymävuosi(vvvv): "))

    vuoden_parit = [int(vuosi) for vuosi in str(vuosi)] # muuttaa vuoden luvut 2:n pareiksi
    kortin_numero = paiva + kuukausi + sum(vuoden_parit) # laskee yhteen syntymäpäivän, syntymäkuukauden ja vuoden numerot
    return kortin_numero # palauttaa kortin numeron

    if 10 <= kortin_numero <= 99:# jos kortin numero on parillinen
        
