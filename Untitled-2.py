import math

num1 = input("Первое число: ")
num2 = input("Второе число: ")

print(f"{math.sqrt(int(num1))} - результат корня 1 числа")
print(f"{math.sqrt(int(num2))} - результат корня 2 числа")
print(f"{float(num1) / float(num2)} - результат деления")
print(f"{float(num1) + float(num2)} - результат сложения")
print(f"{float(num1) - float(num2)} - результат разности")
print(f"{float(num1) * float(num2)} - результат умножения")
print(f"{float(num1)  ** float(num2)} - результат степени")