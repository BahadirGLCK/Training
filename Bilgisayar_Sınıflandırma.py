import random
import time

class bilgisayar():

	def __init__ (self, bilgisayar_durumu, işletim_sistemi, parlaklık, ses):

		self.bilgisayar_durumu = bilgisayar_durumu
		self.işletim_sistemi = işletim_sistemi
		self.parlaklık = parlaklık
		self. ses = ses

	def bilgilerigöster(self):

		print (""" 

			Bilgisayar Durumunuz: {} 
			İşletim Sisteminiz: {}
			Bilgisayar Parlaklığı: {}
			Bilgisayar Ses Düzeyi: {}

			""" . format(self.bilgisayar_durumu,self.işletim_sistemi,self.parlaklık,self.ses))

	def bilgisayardurumu(self, yeni_durum):

		if (self.bilgisayar_durumu == yeni_durum):
			
			print("Bilgisayarınız Zaten ", self.bilgisayar_durumu)

		else:

			self.bilgisayar_durumu = yeni_durum

			print("Bilgisayarınız ", self.bilgisayar_durumu)

	def __str__(self):
		return "İşletim Sisteminiz {}". format (self.işletim_sistemi)

	def parlaklıkseviyesi(self): 

		print ("Şuanlık Parlaklık Seviyesi: ", self.parlaklık)

		print("Parlaklık Seviyesini Arttırmak için '>' azaltmak için '<' sistemden çıkmak için ise ' q'")

		while True:

			isaret = input()

			if isaret == "<":
				self.parlaklık -=1
				print ("Yeni Parlaklık Seviyesi : ", self.parlaklık)

			elif isaret == ">":
				self.parlaklık +=1
				print ("Yeni Parlaklık Seviyesi : ", self.parlaklık)

			elif isaret == "q":
				break

			else:
				print("Yanlıs karakter girdiniz....")

	def sesseviyesi(self):

		print ("Şuanlık Ses Seviyesi: ", self.ses)

		print("Ses Seviyesini Arttırmak için '+' azaltmak için '-' sistemden çıkmak için ise ' q' ")

		while True:

			ses_isaret = input()

			if ses_isaret == "-":
				self.ses -=1
				print ("Yeni Ses Seviyesi : ", self.ses)

			elif ses_isaret == "+":
				self.ses +=1
				print ("Yeni Ses Seviyesi : ", self.ses)

			elif ses_isaret == "q":
				break

			else:
				print("Yanlıs karakter girdiniz....")	

	def __len__(self):
		return " Ses Seviyesi : {}\nParlaklık Seviyesi: {}". format(self.ses,self.parlaklık)

Bilgisayar = bilgisayar("Açık","Windows",0,0)

while True:
	

	print ("""
		****************************
		
		Bilgisayar Bilgi Ekranına Hoşgeldiniz

		0 bilgisayarın şuan ki durumu
		1 bilgisayar durumu değiştir
		2 bilgisayar işletim sistemi
		3 bilgisayar parlaklık 
		4 bilgisayar ses 

		'q' Menüden çıkış

		****************************
		""")

	new= input("İstediğiniz işlemi giriniz: ")

	if new == "q":
		break

	elif new == "0":

		Bilgisayar.bilgilerigöster()

	elif new == "1":
		
		state = input("Please, You want to enter state: ")
		Bilgisayar.bilgisayardurumu(state)

	elif new == "2":
		
		print(Bilgisayar)

	elif new == "3":

		Bilgisayar.parlaklıkseviyesi()

	elif new == "4":

		Bilgisayar.sesseviyesi()

	else:
		print("Wrong chooses")