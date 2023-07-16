BASE = 16
n_inp: int = int(input('Введите число: '))
n = n_inp
res = ''

while n > 0:
    if n % BASE < 10:
        res = str(n % BASE) + res
    else:
        match n % BASE:
            case 10:
                res = res + 'a'
            case 11:
                res = res + 'b'
            case 12:
                res = res + 'c'
            case 13:
                res = res + 'd'
            case 14:
                res = res + 'e'
            case 15:
                res = res + 'f'
    n = n // BASE

print('Результат:', res)
print('Проверка hex():', hex(n_inp)[2:])