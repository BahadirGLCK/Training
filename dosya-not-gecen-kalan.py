def not_hesaplama(satır):
	
	satır = satır[:-1]
	liste = satır.split(",")

	isim = liste[0]
	not1 = int(liste[1])
	not2 = int(liste[2])
	not3 = int(liste[3])
	ortalama = not1*(3/10) + not2*(3/10) + not3*(4/10)

	if (ortalama >= 90):
		harf="AA"
	elif(ortalama >= 85):
		harf ="BA"
	elif(ortalama >= 80):
		harf ="BB"
	elif(ortalama >= 75):
		harf ="CB"
	elif(ortalama >= 70):
		harf ="CC"
	elif(ortalama >= 65):
		harf ="DC"
	elif(ortalama >= 60):
		harf ="DD"
	elif(ortalama >= 55):
		harf ="FD"
	else:
		harf ="FF"

	return isim + "-------------->" + harf + "\n"

def gecenler(satır):

	satır = satır[:-1]
	liste = satır.split(",")

	ad = liste[0]
	harf_notu = liste[2]

	if (harf_notu != "FF" or harf_notu != "FD"):

		return ad + "-------------->" + harf_notu + "\n"

def kalanlar(satır):

	satır = satır[:-1]
	liste = satır.split(",")

	ad = liste[0]
	harf_notu = liste[2]

	if (harf_notu == "FF" or harf_notu == "FD"):

		return ad + "-------------->" + harf_notu + "\n"



with open("dosya.txt","r",encoding="utf-8") as file:

	eklenecekler_listesi = []
	gecenler_listesi = []
	kalanlar_listesi = []
	
	for i in file:
		eklenecekler_listesi.append(not_hesaplama(i))

	with open("harfnotları.txt","w",encoding="utf-8") as file2:
		for i in eklenecekler_listesi:
			file2.write(i)
		
	for i in eklenecekler_listesi:
		gecenler_listesi.append(gecenler(i))

	for i in eklenecekler_listesi:
		kalanlar_listesi.append(kalanlar(i))

	with open("gecenler.txt","w",encoding="utf-8") as file3:
		for i in gecenler_listesi:
			file3.write(i)	

	with open("kalanlar.txt","w",encoding="utf-8") as file4:
		for i in kalanlar_listesi:
			file4.write(i)
			