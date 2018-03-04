#Problem 1
kilo = int(input ("Kilonuzu Giriniz : "))
boy = float (input("Metre Cinsinden Boyunuzu Giriniz: "))

bke= kilo / (boy **2)

if (bke <= 18.5):
	print("Zayıf")
elif (bke <= 25 and bke >= 18.5 ):
	print ("Normal")
elif (bke <= 30 and bke >= 25 ):
	print ("Fazla Kilolu")
elif ( bke >= 30 ):
	print ("Obez")

#Problem 2 
sayi1 = int(input("1. Sayiyi Giriniz :"))
sayi2 = int(input("2. Sayiyiy Giriniz:"))
sayi3=  int(input("3. Sayiyi Giriniz: "))

if (sayi1>sayi2 and sayi1> sayi3):
	print("En Büyük Sayi: ", sayi1)
if (sayi2>sayi1 and sayi2> sayi3):
	print("En Büyük Sayi: ", sayi2)
if (sayi3>sayi2 and sayi3> sayi1):
	print("En Büyük Sayi: ", sayi3)

#Problem 3 
vize1 = int(input("Lütfen 1. Vize Notunuzu Giriniz: "))
vize2 = int(input("Lütfen 2. Vize Notunuzu Giriniz: "))
Final = int(input("Lütfen Final Notunuzu Giriniz : "))

Toplam_Not = (vize1*30/100) + (vize2*30/100) + (Final*40 /100)

if (Toplam_Not >= 90):
	print("AA")
elif (Toplam_Not >= 85):
	print("BA")
elif (Toplam_Not >= 80):
	print("BB")
elif (Toplam_Not >= 75):
	print("CB")
elif (Toplam_Not >= 70):
	print("CC")
elif (Toplam_Not >= 65):
	print("DC")
elif (Toplam_Not >= 60):
	print("DD")
else:
	print("Yazmaya gerek yok")

#Problem 4
sekil = input("Geometrik Sekli belirtiniz: ")

if (sekil == "Dörtgen"):
	kenar1 = int(input("1. Kenarı Giriniz: "))
	kenar2 = int(input("2. Kenarı Giriniz: "))
	kenar3 = int(input("3. Kenarı Giriniz: "))
	kenar4 = int(input("4. Kenarı Giriniz: "))

	if (kenar1 == kenar2 and kenar3==kenar4 and kenar1 == kenar3 and kenar3 == kenar2 ):
		print("Seçtiğiniz şekilin kenarları:{}, {}, {}, {} ve şekliniz kare ".format(kenar1, kenar2, kenar3, kenar4))
	else:
		print("Seçtiğiniz şekilin kenarları:{}, {}, {}, {} ve şekliniz digdörtgen ".format(kenar1, kenar2, kenar3, kenar4))

elif(sekil == "Üçgen"):
	ükenar1 = int(input("1. Kenarı Giriniz: "))
	ükenar2 = int(input("2. Kenarı Giriniz: "))
	ükenar3 = int(input("3. Kenarı Giriniz: "))

	if(ükenar3==ükenar2==ükenar1):
		print("Seçtiğiniz şekilin kenarları:{}, {}, {} ve şekliniz eşkenar üçgen ".format(ükenar1, ükenar2, ükenar3))
	elif((ükenar3==ükenar2) and (ükenar3!=ükenar1)):
		print("Seçtiğiniz şekilin kenarları:{}, {}, {} ve şekliniz ikizkenar üçgen ".format(ükenar1, ükenar2, ükenar3))
	elif((ükenar3==ükenar1) and (ükenar3!=ükenar2)):
		print("Seçtiğiniz şekilin kenarları:{}, {}, {} ve şekliniz ikizkenar üçgen ".format(ükenar1, ükenar2, ükenar3))
	elif((ükenar2==ükenar1) and (ükenar2!=ükenar3)):
		print("Seçtiğiniz şekilin kenarları:{}, {}, {} ve şekliniz ikizkenar üçgen ".format(ükenar1, ükenar2, ükenar3))
	elif((ükenar1==ükenar3) and (ükenar3!=ükenar2)):
		print("Seçtiğiniz şekilin kenarları:{}, {}, {} ve şekliniz ikizkenar üçgen ".format(ükenar1, ükenar2, ükenar3))
	elif(((abs(ükenar1-ükenar2)< ükenar3) and (ükenar3<(ükenar1+ükenar2))) or ((abs(ükenar3-ükenar2)< ükenar1) and (ükenar1<(ükenar3+ükenar2))) or ((abs(ükenar1-ükenar3)< ükenar2) and (ükenar2<(ükenar3+ükenar1)))):
		print("Seçtiğiniz şekilin kenarları:{}, {}, {} ve şekliniz sıradan üçgen ".format(ükenar1, ükenar2, ükenar3))
	else:
		print("Seçtiğiniz kenarlar üçgen oluşturamamaktadır...")
else:
	print("Lütfen Doğru Şekil Giriniz...")

	
	

