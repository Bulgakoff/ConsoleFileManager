import random

min_num = 1
max_num = 100
puzzle = 40
count = 0
# что бы не было такого   while result != '=':
# NameError: name 'result' is not defined
result = None
while result != '=':
    count += 1
    number = random.randint(min_num, max_num)
    print(number)
    result = input('Сказать какой результат < = или >: ')
    if result == '<':
        print(f'Число {number} меньше чем {puzzle} ')
        min_num = number + 1
        print(f'min_num = {min_num}')

    elif result == '>':
        print(f'Число {number} ,больше чем {puzzle} ')
        max_num = number - 1
    else:
        print('введен ошибочный символ повторите ввод ')

print(f'Ура победа Число {number} равно  {puzzle} ')
print(f'Ответ получен за {count} попыток ')
print('END')