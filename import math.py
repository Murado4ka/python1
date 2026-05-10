import math
a = input("Первый катет: ")
b = input("Второй катет: ")
a2 = float(a) ** 2
b2 = float(b) ** 2
c2 = float(a2) + float(b2)
s = float(a) * float(b)
print(f"{math.sqrt(float(c2))} - гипотенуза")
print(f"{float(s) / 2} - площадь")