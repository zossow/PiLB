f = open("tekst9", "r")
tekst = f.read().split()
print(tekst)
zamiana = {'i': 'oraz', 'oraz': 'i', 'Nigdy': 'Prawie nigdy', 'Dlaczego': 'Czemu'}
for i, x in enumerate(tekst):
    if x in zamiana:
        temp = zamiana[x]
        tekst[i] = temp
print(' '.join(tekst))
