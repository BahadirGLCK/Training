a = str("ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb")

ayrı = list()
harf_sozluk = dict()

for i in a :
	ayrı.append(i)
print(ayrı)

for i in ayrı:
	if i in harf_sozluk:
		harf_sozluk[i] +=1
	else:
		harf_sozluk[i] = 1

for kelime,sayı in harf_sozluk.items():

	print("{} Kelimesi {} defa geçiyor". format(kelime,sayı))
	print("********************")
##############################################################

with open("şiir.txt","r",encoding="utf-8") as file:
    liste= list()
    for i in file:
        liste.append(i)
    for i in liste:
       i.strip()
    print(liste)