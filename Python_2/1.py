#Wpisywanie z klawiatury

twoj_tekst = input("Twoj tekst: ")
print('Wpisany tekst brzmi: {}'.format(twoj_tekst))

#Odczytanie pliku

plik_odczyt = open('pliczek.txt','r')
tekst_odczyt = plik_odczyt.read()
print("Odczytuje plik: ", tekst_odczyt)

#Zapis do pliku

plik = open('pliczek.txt','w')
tekst = 'Wpisuje do pliku tekst: ' + twoj_tekst
plik.write(tekst)
plik.close()
