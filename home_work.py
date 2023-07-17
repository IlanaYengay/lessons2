#1
# def sum_digit (n):
#     if n == 1:
#         return 1
#     return sum_digit(n-1) + n

# print(sum_digit(4))

#2
# def max_elem (n):
#     if len(n) == 1:
#         return 0
#     return max(n[0], max_elem(n[1:]))

# print(max_elem([12, 3, 45, 5, 123,  43]))

#4
# def polindrom (stroka):
#     if not stroka:
#         return 'not polindrom'
#     return polindrom (stroka[1:-1])

# print(polindrom('madam'))