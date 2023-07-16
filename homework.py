my_input = (int(input('Введи число, а я определю, простое оно или составное. Но есть одно условие!'
                      ' Нельзя вводить отрицательные числа или числа больше 100.000: ')))

if my_input <= 0 or my_input > 100000:
    print('Ты не читал условие???')
else:
    print()

res = 'Простое'
for x in range(2, my_input):
    if my_input % x == 0:
        res = 'Составное'

print(res)