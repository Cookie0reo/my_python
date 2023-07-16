a = (int(input('Введите сторону а: ')))
b = (int(input('Введите сторону b: ')))
c = (int(input('Введите сторону c: ')))
if a + b > c and a + c > b and c + b > a:
    print('Всё верно! Нету никаких несостыковок :)')
else:
    print("Невозможно!")
if a == b == c:
    print('\nА ещё этот треугольник равносторонний')
elif a == b or a == c or c == b:
    print('\nА ещё этот треугольник равнобедренный')
elif a != b and a != c and c != b:
    print('\nА ещё этот треугольник разносторонний')
else:
    print('')