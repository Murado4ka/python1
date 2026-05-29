total = 0
while True:
    number = int(input("Введи число (0 для выхода): "))
    if number == 0:
        break
    total += number
print(f"Сумма: {total}")
