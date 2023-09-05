def get_second_digit():
    try:
        num = int(input('Введите трехзначное целое число:  '))
       
        num = str(num)
        
        if len(num) == 3:
            my_num = num[1]
            return f'second_digit = {my_num}'
        if  len(num) == 4 and num[0] == '-':
            my_num = num[2]
            return f'second_digit = {my_num}'
        else:
            return'Неверный ввод данных'
        
    except ValueError:
        print('Ошибка воода данных')       

print(get_second_digit())



def get_third_digit():
    try:
        num = int(input('Введите трехзначное целое число:  '))
       
        num = str(num)
        
        if len(num) == 3:
            my_num = num[2]
            return f'третья цифра = {my_num}'
        if  len(num) == 4 and num[0] == '-':
            my_num = num[3]
            return f'третья цифра  = {my_num}'
        if len(num) < 3:
            return 'Третьей цифры нет'
        else:
            return'Неверный ввод данных'
        
    except ValueError:
        print('Ошибка воода данных')       

print(get_third_digit())               
            

def get_my_day():
    try:
        day = int(input('Введите число от одного до семи '))
        if 1 <= day <=7 and day == 7:
            return '7 - Это воскресенье - выходной день'
        if 1 <= day <= 7 and day == 6:
            return '6 - Это суббота - выходной день'
        if 1 <= day <= 7 and day == 5:
            return '5 - "Это пятница - рабочий  день'
        if 1 <= day <= 7 and day == 4:
            return '4 - "Это четверг - рабочий  день'
        if 1 <= day <= 7 and day == 3:
            return '3 - "Это среда  - рабочий  день'
        if 1 <= day <= 7 and day == 2:
            return '2 - "Это вторник  - рабочий  день'
        if 1 <= day <= 7 and day == 1:
            return '1 - "Это понедельник  - рабочий  день'
        if 1 < day > 7:
            return "Неверный ввод данных"
    except ValueError:
        print('Ошибка воода данных')  
print(get_my_day())      
        