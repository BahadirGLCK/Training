#Mükemmel Sayı_Problem1 
Sayı = int(input("Sayı Giriniz: "))
liste = list()
for i in range(1,Sayı):
	print("Seçilene Kadar Olan Sayılar: ", i)
	if (Sayı%i == 0):
		liste.append(i)
print("Sayıların Bölenleri: ", liste)
a=0
for j in liste:
	a +=j
if (a == Sayı):
	print("Mükemmel Sayınız : {}". format(Sayı))
else:
	print("Mükemmel Sayı Seçemediniz ....")

#Armstrong Sayısı_Problem2
sayı = int(input("Sayı:"))

basamak = 0
toplam = 0

gecici_sayı = sayı

while (gecici_sayı > 0):
    
    basamak = gecici_sayı % 10
    
    toplam += basamak ** 4 
    
    gecici_sayı //= 10

if (toplam == sayı):
    print(sayı,"bir armstrong sayısıdır.")
else:
    print(sayı,"bir armstrong sayısı değildir.")
#Problem 3 _ Çarpım Tablosu 
for i in range(10):
	for j in range(10):
		Çarpım = i*j
		print("{}*{} ={} " . format(i,j,Çarpım))
#Problem 4
while True:
	Sayı = input("Sayı Giriniz: ")
	if (Sayı =="q"):
		break
	Sayı1= int(Sayı)
	toplam += Sayı1
print("Sonuç: ", toplam)
#Problem 5
i=0
while (i<101):
    i +=1

	if ((i%3) != 0):
		continue
	else:
		print(i)
