# from functools import reduce
# x, y, z = map(int, input().strip().split())#map вместо цикла
# volume = reduce(lambda x, y: x * y, map(int, input().strip().split()))# reduce вместо цикла
# names = ['Ivan', 'ignat', 'Kirill', 'Vlad']
# names_starts_i = filter(lambda name: name.upper().startswith('I'), names)#filter вместо цикла
# another_names = names[:]#сделать копию списка
# def gcd(a, b):
#     while b > 0:
#         a, b = b, a % b
#     return a
#
# from math import gcd
# from functools import reduce
# first_number = int(input())
# numbers_list = sorted([int(input()) for number in range(first_number)])
# result = reduce(gcd, numbers_list)
# print(result)
