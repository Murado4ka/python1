time = int(input("Сколько у вас сейчас время: "))

if time >= 6 and time <= 11:
    print("Доброе утро!")
elif time >= 12 and time <= 17:
    print("Добрый день!")
elif time >= 18 and time <= 21:
    print("Добрый вечер!")
elif 22 <= time >= 23 or 0 <= time >= 5:
    print("Доброй ночи!")
else:
    print("Я не тупой, такого времени не существует")