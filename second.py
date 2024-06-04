import random

# Генерируем случайное трехзначное число
number = random.randint(100, 999)

# Выводим на экран сгенерированное число
print(number)

# Вычисляем цифры числа
digit_1 = number // 100
digit_2 = (number // 10) % 10
digit_3 = number % 10

# Вычисляем сумму цифр
sum_digits = digit_1 + digit_2 + digit_3

# Вычисляем произведение цифр
product_digits = digit_1 * digit_2 * digit_3

# Выводим на экран сумму и произведение цифр
print("Сумма:", sum_digits)
print("Произведение:", product_digits)
