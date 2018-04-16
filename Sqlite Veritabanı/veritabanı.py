import sqlite3

con = sqlite3.connect("kütüphane.db")
cursor = con.cursor()

def tablo_olusturma():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT, Yazar TEXT,Yayınevi TEXT,Sayfa INT)")
    con.commit()

def veri_ekleme():
    cursor.execute("Insert into kitaplık VALUES('Yalın Yeni Girişim','Eric Ries','Buz Dağı','280')")
    con.commit()
def veri_ekleme2(isim,yazar,yayınevi,sayfa):
    cursor.execute("insert into kitaplık VALUES(?,?,?,?)",(isim,yazar,yayınevi,sayfa))
    con.commit()
    
isim = input("Kitabın İsmini Giriniz: ")
yazar= input("Kitabın Yazarı: ")
yayınevi= input("Yayınevi:")
sayfa = int(input("Sayfa Sayısı: "))

#tablo_olusturma()
#veri_ekleme()
veri_ekleme2(isim,yazar,yayınevi,sayfa)
con.close()
