# stroka = 'Я функция из my_module.py'


# import random
# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
# random_names = []
# for i in range(4): 
#     g = random.choice(names)
#     random_names.append(g)
# print(random_names)

# import sys
# print(sys.platform)


# import os


# import os

# for i in range(5):
#     new_dir = f'/Users/ilanaengaj/Desktop/New_Papka/as{i}'
#     path = os.path.join(new_dir)
#     os.mkdir(path)
#     print(f'Директория {new_dir} создана')

# import os
# for i in range(5):
#     os.system(f'touch /Users/ilanaengaj/Desktop/New_Papka/dir{i}.py')


# import os
# for i in range(5):
#     os.system(f'mkdir /Users/ilanaengaj/Desktop/New_Papka/dir{i}')




# import random

# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
# com1 = []
# com2 = []
# com3 = []
# com4 = []

# for i in names:
#     a = random.choice(names)
#     if a not in com1 and len(com1)<4:
#         com1.append(a)
#     elif a not in com2 and len(com2)<4:
#         com2.append(a)
#     elif a not in com2 and len(com3)<4:
#         com3.append(a)
#     elif a not in com3 and len(com4)<4:
#         com4.append(a)
# print(com1)
# print(com2)
# print(com3)
# print(com4)



# import sys
# print(sys.argv)



#2
# import sys

# user1 = input('Введите число: ')
# user2 = input('Введите число: ')
# size1 = sys.getsizeof(user1)
# size2 = sys.getsizeof(user2)
# if size1 > size2:
#     print('Первое число больше')
# elif size1 < size2:
#     print('Второе число больше')
# else:
#     print('Оба числа весят одинаково')


#!!!
# import random

# password = ''
# user = int(input('Введите число N для пароля: '))
# for i in range(user):
#     password = password + random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
# print('Password:', password)




# повторить #1
# import random

# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
# t1 = []
# t2 = []
# t3 = []
# t4 = []
# for i in (t1, t2, t3, t4):
#     for _ in range(3):
#         i.append(names.pop(random.randint(0, len(names)-1)))
# print (t1)
# print (t2)
# print (t3)
# print (t4)



# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
# print ([[names.pop(random.randint(0, len(names)-1)) for_ in range(3)] for _ in range(4)])


