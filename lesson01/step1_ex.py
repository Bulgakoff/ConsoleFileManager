# функция для создания файла
import os


def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError as d:
        print('МОжно двигаться дальше ', d)


def info_path(files_only=False, fo_only=False):
    result = os.listdir()
    result1 = os.listdir()

    result = [f for f in result if os.path.isdir(f)]

    print(result)


def del_ff(name):
    if os.path.isdir(name):
        os.rmdir(name)  # УДАЛЯЕТ ТОЛЬКО ПАПКИ
    else:
        os.remove('text.js')


# что бы в другом модуле не запускался код
if __name__ == '__main__':
    create_file('text.js')
    create_file('text.js', 'some text')
    create_folder('new_folder4')
    del_ff('new_folder3')

    info_path(True)
# os.remove('text.js')
