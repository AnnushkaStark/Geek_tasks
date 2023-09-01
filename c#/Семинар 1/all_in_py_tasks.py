#a = None
#b = None
def get_min_max():
    try:
        a = int(input('Введите число а:  '))
        b = int(input('Введите число b:  '))

        minimum =min(a,b)
        maximum = max(a,b)
        return f"Минимальное число = {minimum}, максимальное число = {maximum}"
    except ValueError:
        print('Неверный ввод данных')
    except TypeError:
        print('Неверный формат данных')
print(get_min_max())

#a = None
#b = None
#c = None
def get_maximum():
    try:
        my_lst = list(map(int,input('Введите 3 числа через побел: ').split()))
        return f'Максимальное число = {max(my_lst)}'
    except ValueError:
        print('Неверный ввод данных')
    except TypeError:
        print('Неверный формат данных')
print(get_maximum())


#a = None
def is_chet():
    try:
        a =  int(input('Введите число:  '))
        if a % 2 ==0:
            result = 'Это число четное'
        else:
            result = 'Это число не четное'
        return result 
    except ValueError:
        print('Неверный ввод данных')
    except TypeError:
        print('Неверный формат данных')
print(is_chet())

#a= None
def get_chet():
    try:
        a = int(input('Введите число:   '))
        my_lst = [i for i in range(1,a+1) if i % 2 ==0]
        return f'Четные числа от 1 го до вашего числа включительно это {my_lst}'
    except ValueError:
        print('Неверный ввод данных')
    except TypeError:
        print('Неверный формат данных')
print(get_chet())