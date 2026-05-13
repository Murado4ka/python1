import math
m = 25
g = 5
num1 = input("Сколько стоит одна конфета?: ")
num2 = input("Сколько конфет ты хочешь?: ")
print( "Одна конфета стоит " + num1 + "рублей")
print( "Ты хочешь взять " + num2 + "конфет")
print(f"Общая стоимость: {int(num1) * int(num2)}")
print(f"Общий вес: {int(num2) * m}")
c = float(num2) / g
print(f"Нужно упаковок: {math.ceil(c)}")