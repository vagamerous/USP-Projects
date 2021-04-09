import math

a= float(input("digite valor de a: "))

b= float(input("digite valor de b: "))

c= float(input("digite valor de c: "))

delta= float(b**2 - 4*a*c)

x1= (-b + math.sqrt(delta))/2*a

x2= (-b - math.sqrt(delta))/2*a

if delta>0:
    print("possui duas raízes reais,", x1, "e", x2)

else:
    if delta==0:
        print("possui uma raíz real,", x1)
    else:
        print ("essa equação não possui raízes reais")
