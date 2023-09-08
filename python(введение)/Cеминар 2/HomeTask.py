import random

def coin():
    '''Это функция первой задачи, показывает какие монетки быстрее перевернуть'''
    try:
        my_lst = ["Орел","Решка"]
        lst = []
        n = int(input('Сколько раз вы хотите бросить монетку, введите число:   '))
        for _ in range(n+1):
            lst.append(random.choice(my_lst))
        if lst.count("Орел") < lst.count("Решка"):
            return f' Монеток орлом выпало меньше, нужно перевернуть {lst.count("Орел")}'
        if  lst.count("Решка") < lst.count("Орел"):
            return f' Монеток решкой выпало меньше, нужно перевернуть {lst.count("Решка")}'
        if lst.count("Орел") == lst.count("Решка"):
            return f'Выпало одинаковое количество орла и решки, вы можете перевернуть {lst.count("Решка")} любых монет'

    except ValueError:
        return 'Вы ввели не число'
    except KeyboardInterrupt:
        return "Ведены не все данные"
print(coin())

def watermelon_for_tescha():
    '''Эта функция решает впрос с арбузом для тещи'''
    try:
        lst = []
        n = int(input('Ведите количество арбузов в магазине: '))
        for _ in range(n+1):
            lst.append(random.randint(1,100))
        return f"Самый легкий арбуз весит {min(lst)} кг а самый большой {max(lst)}"
    except ValueError:
        return 'Вы ввели не число'
    except KeyboardInterrupt:
        return "Ведены не все данные"
print(watermelon_for_tescha())

def guess_numbers():
    '''Эта функция находит 2 загаданных числа'''
    try:
        num1 = int(input('Ведите первое число от 1 го до 1000  '))
        num2 = int(input("Введите второе число от 1 го до 1000  "))
        p =  int(input('Ведите произведение ваших чисел   '))
        s =  int(input("Введите сумму ваших чисел   "))
        if 1<= num1 <= 1000 and 1<=num2 <= 1000 and num1 + num2 == s and num1 * num2 == p: 
            for num1 in range(1, min(s, p) + 1):
                num2 = s - num1
                if num1 * num2 == p:
                    return f'Вы загадали числа {num1}  и {num1}'
                
        else:
            return f'Ваши числа не подходят под условие'
    except ValueError:
        return 'Вы ввели не число'
    except KeyboardInterrupt:
        return "Ведены не все данные"

print(guess_numbers())

def pow_two():
    '''Эта функция возвращает целые степени двойки от 1 го до введенного числа'''
    try:
        n = int(input('Введите число:  '))
        lst = []
        lst1 = []
        lst =[2**i for i in range(1,n)]
        lst1 = [2**i for i in range(1,n) if 2**i < n]
        if  len(lst) != 0 and len(lst1) !=0:
            return f' Целые степени двойки от одного до введенного числа это  - {lst},Целые степени двойки от одного до введенного числа не превосходящие это число это {lst1}'
        elif  len(lst) != 0 and len(lst1) ==0:
            return f' Целые степени двойки от одного до введенного числа это  - {lst},Целые степени двойки от одного до введенного числа не превосходящие это число это отсутствуют'
        elif len(lst) == 0:
            return 'Целые степени двойки от одного до вашего числа отсутствуют'
            
    except ValueError:
        return 'Вы ввели не число'
    except KeyboardInterrupt:
        return "Ведены не все данные"
print(pow_two())
