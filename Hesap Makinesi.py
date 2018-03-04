sayi1 = float(input("Sayı Giriniz: "))
islem = input("İslem seçiniz: ")
sayi2 = float(input("Sayı Giriniz: "))

if (islem == "Çarpma"):
     print("Sonuç : \n", sayi1* sayi2)
elif(islem == "Bölme"):
    print("Sonuç : \n", sayi1/ sayi2)
elif(islem == "Toplama"):
    print("Sonuç : \n", sayi1+ sayi2)
elif(islem == "Çıkartma"):
    print("Sonuç : \n", sayi1- sayi2)
else:
    print("Lütfen Doğru İşlem Seçiniz: ")
