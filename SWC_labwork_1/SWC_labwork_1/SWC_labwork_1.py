import math

a = input("Введите значение А: ")
b = input("Введите значение B: ")
c = input("Введите значение С: ")
D = b**2 - complex(4*a*c)
print("D = " + str(D))
x1 = (-b+D**0.5)/(2*a)
x2 = (-b-D**0.5)/(2*a)