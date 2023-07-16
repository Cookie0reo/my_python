from random import randint
nam = randint(0, 1000)
i = 0
while i < 10:
    my_input = (int(input("Я загадал число от 0 до 1000! Попробуй отгадать! ")))
    if my_input == nam:
        print('Вау! Ты угадал! Только медальку делай сам)))')
    elif my_input < nam:
        print('Больше!')
    elif my_input > nam:
        print('Меньше!')
    i+=1

print(f'Упс! У кого-то закончились попытки! Загаданным числом было: {nam}')