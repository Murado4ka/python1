import random
sec_num = random.randint(1, 10)
print("Я загадал число от 1 до десяти попробуй отгадать")
guess = int(input("твоё число: "))
while True:
    guess = int(input("твоё число: "))
    if guess != sec_num:
       print ("Ты угадал❤")
       break
    else:
        print("нет не так❤")