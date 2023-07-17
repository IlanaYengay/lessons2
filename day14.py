# #№1
# def main(n: int):
#     if n == 1:
#         return 1
#     return main(n-1) + n




# print(main(3))

# $3 = $2 + 3
# $2 = $1 = 1

# рекурсия - чтобы ее использовать, нужно вызвать функцию внутри себя
# для возвращения кода

#№2
# def number (n: int):
#     if n < 10:
#         return 1
#     return number (n // 10) + 1 



# print (number(14))


#№3
# def number (n, m):
#     if m == 0:
#         return 1
#     return number(n,m-1)*n
    


# print(number(2, 3))


#4
# def spisok (num):
#     if len(num) == 1:
#         return num[0]
#     return min(num[0], spisok(num[1:]))

# print(spisok([12, 4, 654, 67]))


# def spisok(num):
#     if len(num) == 1:
#         return num[0]
#     else:
#         return min(num[0], spisok(num[1:]))
    
# print(spisok([12, 3, 55]))

#5
# def kol_elem(elem):
#     if not elem:
#         return 0
#     return 1 + kol_elem(elem[1:])

# print(kol_elem([9, 23, 4, 66, 77, 45, 6]))


#6
# def spisok (elem):
#     if len(elem) == 1:
#         return [elem[0]]
#     return [elem[-1]] + spisok(elem[:-1])

# print(spisok(['ilana', 'chingiz', 'adil', 'leila']))


#


# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
    
# print(factorial(4))



