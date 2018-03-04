print("Denklem = ax^2 + bx +c")

a = int(input("a sayısını giriniz: "))
b = int(input("b sayısını giriniz: "))
c=  int(input("c sayısını giriniz: "))


delta = b**2 - 4 * a * c
print("DELTA: ", delta)

x1= (- b - delta ** 0.5) / (2 * a)
x2= (- b + delta ** 0.5) / (2 * a)

print("1. Kök :{} \n2. Kök :{}".format(x1,x2))

