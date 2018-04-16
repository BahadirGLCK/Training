#Mükemmel Sayı
def mükemmel(sayı):
	toplam = 0
	for i in range(1,sayı):
		if (sayı%i == 0):
			toplam +=i
	if (toplam == sayı):
		print("SAYI :{} Mükemmle Sayı". format(sayı))
	else:
		return print("Mükemmle sayı Değil")

while True:
	sayı = input("Sayı:")

	if (sayı =="q"):
		print("Programdan çıkma işlemi gerçekleştirdiniz...")
		break
	else:
		sayı = int(sayı)
		mükemmel(sayı)

#Ebob BULMA
def ebob_bulma(sayı1,sayı2):
    
    i = 1
    ebob = 1
    while (i <= sayı1 and i <= sayı2 ):

        if ( not (sayı1 % i) and not (sayı2 % i)):
            ebob = i
        i += 1
    return ebob
sayı1 = int(input("Sayı-1:"))
sayı2 = int(input("Sayı-2:"))

print("Ebob:",ebob_bulma(sayı1,sayı2))



