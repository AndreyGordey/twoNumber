# Ввод двух чисел
x = int(input('введите число: '))
y = int(input('введите второе число: '))

# Вывод значений переменных до обмена
print("x =", x, ", y =", y)

# Обмен значений переменных
x, y = y, x

# Вывод значений переменных после обмена
print("x =", x, ", y =", y)
