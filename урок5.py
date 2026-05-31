import random
print("=" * 40)
print("||" + " " * 10 + "Угадай число 2.0" + " " * 10 + "||")
print("=" * 40)
print("\nДобро пожаловать в улучшенную версию класической игры!")
print("\nМеню")
print("-" * 30)
print("1. Одиночная игра против компютера")
print("2. Парная игра с другом")
print("3. Выход")
print("-" * 30)
while True:
    choice = input("\nВыберите действие(1-3): ")
    if choice != "1" and choice != "2" and choiсe != "3":
        print("Ошибка. Введи число от 1 до 3. Попробуй еще раз.")
        continue
    if choice == "1":
        print("Ты играешь с пк")
        sec_num = random.randint(1, 100)
        attempts = 0
        max_attempts = None
        limit_choice = input("Установить лимит попыток? да или нет? ")
        if limit_choice == "да":
            max_attempts = int(input("Введи количество попыток: "))
        print("Компьютер загадал число от 1 до 100. Попробуй угадать!")
        while True:
            guess = int(input("Ваша догадка: "))
            attempts += 1
            if guess < sec_num:
                print("Число больше")
            elif guess > sec_num:
                print("Число меньше")
            else:
                print("Поздравляю ты угадал!")
                break
            if max_attempts and attempts >= max_attempts:
                print(f"Попытки закончились. Загаданное число = {sec_num}.")
                break
    elif choice == "2":
        print("\n=== Парный режим ===")
        print("Игрок 1 загадывает число, Игрок 2 угадывает")
        secret_number = int(input("Игрок 1, введите число от 1 до 100: "))
        attempts = 0
        max_attempts = None

        limit_choice = input("Установить лимит попыток? (да/нет): ").lower()
        if limit_choice == "да":
            max_attempts = int(input("Введите максимальное количество попыток: "))

        print("Игрок 2, начинайте угадывать!")

        while True:
            guess = int(input("Ваша догадка: "))
            attempts += 1

            if guess < secret_number:
                print("Загаданное число БОЛЬШЕ!")
            elif guess > secret_number:
                print("Загаданное число МЕНЬШЕ!")
            else:
                print(f"Игрок 2 угадал число за {attempts} попыток!")
                break
            if max_attempts and attempts >= max_attempts:
                print(f"Попытки закончились! Загаданное число было {secret_number}.")
                break
    elif choice == "3":
        print("Спасибо за игру! Пока")