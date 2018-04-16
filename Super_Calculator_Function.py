 import mathlibrary

 n= int (input("Please, May ı give your Number: "))
 a= int (input("Please, May ı give your Number: "))
 calculate= input("Which calculate method do you want? ")

 if (calculate== "çarpma") :
 	print(mathlibrary.çarpma(n,a))
 elif(calculate =="toplama"):
 	print(mathlibrary.toplama(n,a))
 else:
 	print("Please, Can you try toplama or çarpma")

