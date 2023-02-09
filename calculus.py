print('КАЛЬКУЛЯТОР групи 12.01 Python Dev 09-11')


def power(a, n):
    return a ** n


def square_root(a):
    return round(power(a, 1/2), 3)


def cube_root(a):
    return round(power(a, 1/3), 3)


def ask_power_base():
    return float(input('Введіть основу степеня '))


while True:
    print('''** Піднесення до степеня \n\t2r Корінь квадратний \n\t3r Корінь кубічний ''')

    action = input('Виберіть будь ласка дію, або напишіть \'bye\' щоб вийти з програми \n')
    match action:
        case 'bye':
            break
        case '**' | '2r' | '3r':
            c = ask_power_base()
            match action:
                case '**':
                    result = power(c, float(input('Введіть показник степеня ')))
                case '2r':
                    result = square_root(c)
                case '3r':
                    result = cube_root(c)
        case _:
            print('Обчислення цієї дії зараз недоступне', end='\n\n')
            continue
    print(result, end ='\n\n')
