import random

#


# def main():



def game_guess():
    puzzle_num = random.randint(1, 50)
    attempts = 0
    print(puzzle_num)
    guess_num = None

    while cond(attempts, guess_num, puzzle_num):
        guess_num = int(input('Введите свой ответ : '))
        attempts += 1
        if puzzle_num < guess_num:
            print(f'attempts № {attempts} ')
            print('Вы ввели больше ')
        elif puzzle_num > guess_num:
            print(f'attempts № {attempts} ')
            print('Вы ввели меньше ')
        elif puzzle_num == guess_num:
            print(f'attempts № {attempts} ')
            print(f'Вы угадали!!! за {attempts} попыток')
            break

    else:
        print(f'Вы потратили все {attempts} попыток - ПРОИРЫШ!!!')

    print('GAME OVER')


def cond(a, g, p):
    return a < 6 and g != p


if __name__ == '__main__':
    game_guess()


# main()
