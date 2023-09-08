from math import sqrt
def distance():
    try:
        x1 = int(input("Введите координату х1  "))
        x2 = int(input("Введите координату х2  "))
        y1 = int(input("Введите координату y1  "))
        y2 = int(input("Введите координату y2  "))
        z1 = int(input("Введите координату z1  "))
        z2= int(input("Введите координату z2  "))
        result = sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
        return f'Расстояние между вашими координатами в 3D пространстве  = {result}'
    except ValueError:
        return 'Неверный ввод данных'
    except TypeError:
        return 'Неверный ввод данных'
    except KeyboardInterrupt:
        return 'Вы ввели не все данные'
print(distance())

def cubes():
    try:
        n = int(input("Ведите число  "))
        cubes = [i**3 for i in range(1,n+1)]
        return f'Кубы целых чисел от 1 го до вашего числа  это {cubes}'
    except ValueError:
        return 'Неверный ввод данных'
    except TypeError:
        return 'Неверный ввод данных'
    except KeyboardInterrupt:
        return 'Вы ввели не все данные'
    
print(cubes())


def palindorm():
    try:
        s = input('Введите 5 ти значное число  ')
        if s.isdigit() and len(s) < 5:
            result = 'Число слишком маленькое'
        if  s.isdigit() and len(s) > 5:
            result = 'Число слишком большое'
        if  s.isdigit() == False:
            result = 'Это не число'
        if len(s) == 5 and s.isdigit() and s == s[::-1]:
            result = 'Это палиндорм'
        if len(s) == 5 and s.isdigit() and s != s[::-1]:
            result = 'Это  не палиндорм'
        return result
    except ValueError:
        return 'Неверный ввод данных'
    except TypeError:
        return 'Неверный ввод данных'
    except KeyboardInterrupt:
        return 'Вы ввели не все данные'
print(palindorm())
    