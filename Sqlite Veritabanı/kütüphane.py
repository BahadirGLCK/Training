import sqlite3

import time

class Kitap():

	def __init__(self,isim,yazar,yayınevi,tür,baskı):

		self.isim = isim
		self.yazar = yazar
		self.yayınevi = yayınevi
		self.tür = tür
		self.baskı = baskı

	def __str__(self):

		return "Kitap İsmi = {}\nYazar İsmi = {}\nYayınevi = {}\nTür = {}\nBaskı = {} ". format(self.isim,self.yazar,self.yayınevi,self.tür,self.baskı)

class Kütüphane():

	def __init__(self):

		self.baglantı_olustur()

	def baglantı_olustur(self):

		self.baglantı = sqlite3.connect("Kütüphane.db")
		self.cursor = self.baglantı.cursor()

		self.cursor.execute("CREATE TABLE IF NOT EXISTS kitaplar (isim TEXT, yazar TEXT, yayınevi TEXT, tür TEXT, baskı INT)")
		self.baglantı.commit()

	def baglantıyı_kes(self):

		self.baglantı.close()

	def kitapları_goster(self):

		self.cursor.execute("Select * From kitaplar")
		kitaplar = self.cursor.fetchall()

		if (len(kitaplar)==0):
			print("Kütüphanede Kitap Bulunmamaktadır")
		else:
			for i in kitaplar:

				kitap = Kitap(i[0],i[1],i[2],i[3],i[4])
				print(kitap)

	def kitap_sorgula(self,isim):

		self.cursor.execute("Select * From kitaplar where isim = ? ",(isim,))
		kitaplar = self.cursor.fetchall()

		if (len(kitaplar)==0):
			print("Bu isimde kitap bulunmamaktadır...")
		else: 
			kitap = Kitap(kitaplar[0][0],kitaplar[0][1],kitaplar[0][2],kitaplar[0][3],kitaplar[0][4])
			print(kitap)

	def kitap_ekle(self,kitap):

		self.cursor.execute("Insert into kitaplar Values (?,?,?,?,?)",(kitap.isim,kitap.yazar,kitap.yayınevi,kitap.tür,kitap.baskı))
		self.baglantı.commit()

	def kitap_sil(self,isim):

		self.cursor.execute("Delete From kitaplar where isim = ?", (isim,))
		self.baglantı.commit()

	def baskı_yükselt(self,isim):

		self.cursor.execute("Select * From kitaplar where isim = ? ", (isim,))

		kitaplar = self.cursor.fetchall()

		if (len(kitaplar)== 0 ):
			print("Böyle bir kitap bulunmamaktadır...")
		else:
			baskı = kitaplar [0][4]
			baskı +=1

			self.cursor.execute("Update kitaplar set baskı = ? where isim = ? ", (baskı,isim))
			self.baglantı.commit()





		
