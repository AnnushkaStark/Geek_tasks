import random

def chet_numbers():
    '''Эта функция выводит количество четных чисел в массиве'''
    try:
        n = int(input('Введите длину массива   '))
        arr = [random.randint(100,999) for _ in range(n)]
        res = list(filter(lambda x : x if x % 2 == 0 else None,arr))
        if len(res) >0:
            return f'четные числа в вашем массиве - {res}'
        return 'В вашем массиве нет четных чисел'
    except ValueError:
        return 'Неверный ввод даных'
    except TypeError:
        return 'Неверный ввод данных'
    except KeyboardInterrupt:
        return 'Вы не ввели длину масива'
    
print(chet_numbers())

def summ_odd__position_numbers():
    '''Эта функция находит сумму чисел в массиве на нечетных позициях'''
    try:
        n =  int(input('Введите длину массива   '))
        count = 0
        arr = [random.randint(0,1000)for _ in range(n)]
        res =[count + value for counter,value in enumerate(arr) if counter % 2 != 0]
        if sum(res) > 0:
            return f'Сумм нечетных чисел в масссиве {sum(res)}'
        return 'В массиве нет нечетных чичсел'
    except ValueError:
        return 'Неверный ввод даных'
    except TypeError:
        return 'Неверный ввод данных'
    except KeyboardInterrupt:
        return 'Вы не ввели длину масива'

print(summ_odd__position_numbers())

def float_differetnce():
    '''Эта функция находит  разницу между минимальным и макимальным элеменом массива действительных чисел'''
    try:
        n = int(input('Введите длину массива   '))
        arr =[random.uniform(0,1000)for i in range(n)]
        if min(arr) != max(arr):
            return f'Разница между максимальным и минимальным элементом массива {max(arr)-min(arr)}'
        return f'{min(arr)} = {max(arr)} разница 0 - это массив из одного числа '
    except ValueError:
        return 'Неверный ввод даных'
    except TypeError:
        return 'Неверный ввод данных'
    except KeyboardInterrupt:
        return 'Вы не ввели длину масива'
print(float_differetnce())