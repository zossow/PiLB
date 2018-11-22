f = open("tekst9", "r")
tekst = f.read().split()
print(tekst)
kluczowe = ['oraz', 'i', 'Nigdy', 'sie', 'Dlaczego']
for x in tekst:
    if x in kluczowe:
        tekst.remove(x)
print(tekst)
