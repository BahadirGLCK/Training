#Veri Yapıları Problem 1 
a= int(input("a sayısını giriniz: "))
b= int(input("b sayısını giriniz: "))
c= int(input("c sayısını giriniz: "))
print("Sonuç: ", a*b*c)

# Veri Yapıları Problem 2 
boy= float(input("Boyunuzu girin: "))
kilo= int(input("Kilonuzu Girin: "))

print("Kitle Endeksiniz : ", kilo/boy**2)

# Veri Yapıları Problem 3 
km_basına_yaktıgı = float(input("Kilometre Başına Yaktığınız Değer: "))
yol = int(input("kaç km gittiniz:"))

print("Ödemeniz Gereken Miktar: ", yol* km_basına_yaktıgı)

#Veri Yapıları Problem 4 
ad = input("Adınız: ")
soyad = input("Soyadınız: ")
telefon = input("Telefon: ")

liste = [ad, soyad, telefon]

print("Adınız: {}\nSoyadını: {}\nTelefonunuz: {}\n".format(liste[0],liste[1],liste[2]))

#Veri Yapıları Problem 5 
a = input("Lütfen bir adet sayı giriniz")
b= input("Lütfen bir adet sayı giriniz")

a,b = b,a

print("a :{}\n b : {}\n ".format(a,b))

#Veri Yapıları Problem 6 
a= int(input("Birinci Kenar: "))
b= int(input("İkinci Kenar: "))

hip= (a ** 2 + b ** 2 )** 0.5
print("Üçgenin Hipotenüsü: ", hip)

#Benim Problemim
sayi = int(input("Lütfen Çapmak istediğiniz sayı adedini giriniz: "))

