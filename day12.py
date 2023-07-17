# numbers = input("Введите числа через пробел: ").split()
# numbers = list(map(int, numbers))
# print(numbers)


# pow - возводит в степень

# numbers = [1, 2, 6, 3, 8, 5, 9, 4]
# list_filter = list(filter(lambda x: x > 5, numbers))
# print (list_filter)


# a = [1, 3, 4, 5]
# b = ['a', 'b', 'c', 'd']
# print(list(zip(a,b)))


# all - возвращает если все значения Тру
# any - возвращает если хоть одно значение Тру
# round - округляет число в большую сторону
# eval - принимает пайтон код и выполняет его


# a = set()
# for i in range(5):
#     i = int(input("Enter a number: "))
#     a.update(i)
#     print(a)


# numbers = [1,2,3,4,5]
# numbers1 = list(map(lambda x: x**2, numbers))
# print(numbers1)

# names = ['Alice', 'Bob', 'Charlie']
# ages = [25, 30, 35]
# print(list(zip(names, ages)))

# numbers = [2, 4, 6, 8, 9]
# numbers1 = [True if i % 2 == 0 else False for i in numbers]
# print(all(numbers1))

# number = 3.14159
# print(round(number, 2))


# numbers = [-2, -5, 0, 7, -1, 9, 4]
# a = list(filter(lambda x: x>0, numbers))
# print(a)


# numbers = [2, 4, 6, 8, 9]
# numbers1 = all (map(lambda x: x % 2 ==0, numbers))
# print (numbers1)


# text = 'i want to improve my Python skill'
# a = list(filter('a', 'e', 'i', 'o', 'u' ))
# print(a)


# expression = "2 * (3 + 4)"
# print(eval(expression))

# ERROR
# users = {
#     'name': 'Anton'
# }
# try:
#     print(a['age'])
# except KeyError as e:
#     print ('Мы отловили KeyError', e)
# except NameError as e:
#     print('Вы не создали переменную!', e) 
# else:
#     print('Все ок! 200')
# finally:
#     print('Обработка ошибок завершена')


# while True: 
#     try:
#         print(eval(input('>>>')))
#     except ZeroDivisionError as e:
#         zero_except +=1
#         print('Вы пытаетесь делить на ноль')
#     if zero_except == 3:
#         print



#1
# import random

# while True:
#     try: 
#         user = int(input('Отгадайте число: '))
#     except ValueError:
#         print('Введите цифру')
#         continue
#     a = random.randint(0, 10)
#     print(a)
#     if user == a:
#         print('Вы отгадали число')
#     else:
#         print('Вы не отгадали число')



#2
# stroka = ('12', '324', '1234', 'fdsf', 'fjfld')
# import random
# print('Выбор случайной строки из списка: ', random.choice(stroka))


#3
# import random


# while True:
#     try:
#         user = int(input('Enter number 0-1000: '))
#     except ValueError:
#         print('Введите цифру')
#         continue
#     a = random.randint(0, 1000)
#     print(a)
#     if user < a or user > a:
#         print('Слишком мало' or 'Слишком много')


#4
# import random


# number = ()
# try:
#     print('Выбор случайного числа: ', random.choice(number))
# except IndexError:
#     print ('Вы ошиблись')

#5
# import random
# print('Вывод случайного числа от 0 до 1: ')
# print(random.random())
# print(random.random())

#6
