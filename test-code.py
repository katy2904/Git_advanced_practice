name = input('what is your name: ')
print(f'hi, {name}! how are you?')


"""
Задача 5
Дано число. Проверить, кратно ли оно 5 и 10 или 15 но не 30
"""

num = int(input('Введите число: '))

print((num % 5 == 0 and num % 10 == 0) or (num % 15 == 0 and num % 30 != 0))