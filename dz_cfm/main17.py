#
# Практическое задание
# 1. В консольный файловый менеджер добавить проверку ввода
# пользователя для всех функции с параметрами (на уроке разбирали на примере одной функции).
# 2. Добавить возможность изменения текущей рабочей директории.
# 3. Добавить возможность развлечения в процессе работы с менеджером.
# Для этого добавить в менеджер запуск одной из игр: “угадай число” или “угадай число (наоборот)”.
import sys
from core import create_file, create_folder, del_ff, info_path, copy_ff, save_data, change_currdir
from guess_n2 import game_guess
from game_reverse import guess_reverse

save_data('Start')
try:
    command = sys.argv[1]
except IndexError as e:
    print(f'--нужно имя файла ->[{e}')
else:
    print('лсд работает')
    if command == 'info':
        info_path()
    elif command == 'create_f':
        try:
            name = sys.argv[2]
        except IndexError as a:
            print(f'====>{a}')
        else:
            print('all right  create_file!!!!!!!')
            create_file(name)
    elif command == 'create_ff':
        try:
            name = sys.argv[2]
        except IndexError  as z:
            print(f'---> укажите что создать {z}')
        else:
            create_folder(name)


    elif command == 'del':
        try:
            name = sys.argv[2]
        except IndexError as q:
            print(f'---> укажите что удалять {q}')
        else:
            del_ff(name)
    elif command == 'ch':
        try:
            name = sys.argv[2]
        except IndexError as e:
            print(f'---> Нужно ввести имя папки {e}')
        else:
            change_currdir(name)

    elif command == 'copy':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except IndexError as d:
            print(f'--нужно что на что .copy(...)-> {d}')
        else:
            print('all right !!!')
            copy_ff(name, new_name)

    elif command == 'help':
        print('помощь')
    elif command == 'gure':
        guess_reverse()
    elif command == 'gun':
            game_guess()

    save_data('FInish ')
