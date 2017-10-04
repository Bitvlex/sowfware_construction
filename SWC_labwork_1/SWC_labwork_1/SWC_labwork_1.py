import math

a = complex(input("Введите значение А: "))
b = complex(input("Введите значение B: "))
c = complex(input("Введите значение С: "))
D = b**2 - 4*a*c
print("D = " + str(D))
x1 = (-b+D**0.5)/(2*a)
x2 = (-b-D**0.5)/(2*a)
print("x1 = "+str(x1))