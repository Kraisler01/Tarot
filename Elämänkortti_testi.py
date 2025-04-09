def elämänkortti(tiedosto, kortin_numero, kortti_parit):

    paiva = int(input("Anna syntymäpäivä (pp): "))
    kuukausi = int(input("Anna syntymäkuukausi(kk): "))
    vuosi = int(input("Anna syntymävuosi(vvvv): "))


    vuoden_parit = [int(vuosi) for vuosi in str(vuosi)] # muuttaa vuoden luvut 2:n pareiksi
    
    kortin_numero = paiva + kuukausi + sum(vuoden_parit) # laskee yhteen syntymäpäivän, syntymäkuukauden ja vuoden numerot

    if 10 <= kortin_numero <= 99: # tarkistaa, että kortin numero on kahden numeron luku
        kortin_numero = sum(int(kortin_numero) for kortin_numero in str(kortin_numero)) # muuttaa yhteenlasketun summan erillisiksi luvuiksi ja laskee yhteen
        

 #poikkeukset, jotka eivät mene yhteen kortti parien kanssa
 #eli lasketaan eka normi kortit ja jos luku on 2 lukuinen niin ensimmäinen summa on 2 lukuinen 
 #sen summa on eka kortti ja korttiparit ovat poikkeukset tässä alapuolella


    elif kortin_numero == 8:
        Kortti_parit = 17

    elif kortin_numero == 19:
        kortti_parit = #maagikko 3 korttia, kortti 1,10,19
    elif kortin_numero == 10:
        kortti_parit = 1

    elif kortin_numero == 11:
        kortti_parit = 2
    elif kortin_numero == 20:
        kortti_parit = 2

    elif kortin_numero == 12:
        kortti_parit = 3
    elif kortin_numero == 21:
        kortti_parit = 3





