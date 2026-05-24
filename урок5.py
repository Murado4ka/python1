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



