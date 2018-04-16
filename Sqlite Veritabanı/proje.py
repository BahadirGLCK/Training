from kütüphane import *

print("""
****************************************
Kütüphane Programına Hoşgeldiniz

Yapmak İsteğeceğiniz İşlem Numaraları ve Açıklamaları: 
 
1. Kitapları Göster
2. Kitap Sorgulama
3. Kitap Ekle 
4. Kitap Sil 
5. Baskı Yükselt

İşlemi sonlandırmak için 'q' ya basını

****************************************
	""")

kütüphane = Kütüphane()

while True:

	işlem = input("Yapmak İstediğiniz İşlem : ")

	if (işlem == "q"):

		print("Sistemden Çıkılıyor ....")
		time.sleep(2)
		break

	elif (işlem == "1"):
		kütüphane.kitapları_goster()

	elif (işlem == "2"):
		isim = input("Sorgulamak İstediğiniz Kitabı Giriniz: ")
		print("Kitabınız Sorgulanıyor")
		time.sleep(2)

		kütüphane.kitap_sorgula(isim)


	elif (işlem == "3"):
		isim = input("Kitabın İsmi: ")
		yazar = input("Yazar: ")
		yayınevi = input("Yayınevi: ")
		tür = input("Türü: ")
		baskı = input("Baskı Sayısı: ")

		print ("Kitabınız ekleniyor...")
		time.sleep(2)

		yeni_kitap = Kitap(isim,yazar,yayınevi,tür,baskı)
		kütüphane.kitap_ekle(yeni_kitap)
		print("Kitabınız Eklendi")

	elif (işlem == "4"):
		isim = input("Silmek istediğiniz kitabın ismini giriniz: ")
		secim = input("Silmek istediğinizden emin misiniz ? E/H ")

		if (secim == "E"):
			print("Kitabınız Siliniyor...")
			time.sleep(2)

			kütüphane.kitap_sil(isim)
			print("Kitabınız Silindi")
		else:
			print("Kitap silme işlemi iptal edildi ")

	elif (işlem == "5"):
		isim= input("Baskısını Yükseltmek İStediğiniz Kitabı Giriniz : ")

		print("Baskı Yükseltiliyor...")
		time.sleep(2)

		kütüphane.baskı_yükselt(isim)
		print("Baskı Yükseltildi")

	else: 
		print("Lütfen Doğru işlem seçimi yapınız ")