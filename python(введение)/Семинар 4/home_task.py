import random

def find_unical_numbers():
    ''''Эта функция находит уникалные числа входящие в оба списка '''
    try:
        n = int(input('Введите количество чисел в первом списке  '))
        m = int(input('Введите количество чисел во втором списке   '))
        lst1 = [random.randint(1,100) for _ in range(n)] 
        lst2 = [random.randint(1,100) for _ in range(m)]
        result = set(lst1) & set(lst2)
        if len(result) == 0:
            return f"Уникальные числа входящие в оба списка не найдены ({set(lst1)} и {set(lst2)}) - не пересекаются"
        return f'{set(lst1) & set(lst2)} - Это уникальные числа входящие в обя списка '
    except TypeError:
        return 'Неверный ввод данных'
    except ValueError:
        return 'Нверный ввод данных'
    except KeyboardInterrupt:
        return 'Вы ввели не все данные'

print(find_unical_numbers())

def bluberry_harvest():
    '''Эта функция находит сколько ягод собрано за 1 заход'''
    try:
        m = int(input('Введите количество кустов   '))
        bushes = [random.randint(1,100) for _ in range(m)]
        n = len(bushes)
        max_harvest = 0

        for i in range(n):
            harvest = bushes[i] + bushes[(i+1) % n] + bushes[(i+2) % n]
            max_harvest = max(max_harvest, harvest)
        return f'Максимальное количество ягод собранное за один заход платформы это {max_harvest}'
    except TypeError:
        return 'Неверный ввод данных'
    except ValueError:
        return 'Нверный ввод данных'
    except KeyboardInterrupt:
        return 'Вы ввели не все данные'
print(bluberry_harvest())