from fractions import Fraction

input1 = (str(input('Введите первую дробь a/b: ')))
input2 = (str(input('Введите вторую дробь a/b: ')))

int1 = input1.split('/')
int2 = input2.split('/')

a = int(int1[0])
a2 = int(int1[1])
b = int(int2[0])
b2 = int(int2[1])

ch = a * b2 + b * a2
z = a2 * b2
print(f'\nСумма дробей = {ch}/{z}')

ch2 = a * b
z2 = a2 * b2
print(f'Произведение дробей = {ch2}/{z2}')

print("\nПроверка!")
a3 = Fraction(a, a2)
b3 = Fraction(b, b2)
print('Сумма: ', a3 + b3 )
print('Произведение: ', a3 * b3 )