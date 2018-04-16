def çarp(demet):
	return demet[0]*demet[1]
	

liste = [(3,4),(10,3),(5,6),(1,9)]

alan = list(map(çarp,liste))

print(alan)
##########################


##########################
liste = [1,2,3,4,5,6,7,8,9,10]

ciftler =list(filter(lambda x : x%2 == 0 , liste))
toplam = 0
for i in ciftler:
	toplam +=i
print("Çift Sayıların Toplamı = ", toplam)
##########################

isimler = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
Soyisimler= ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

list(zip(isimler,Soyisimler))
