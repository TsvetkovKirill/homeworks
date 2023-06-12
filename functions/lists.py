

# from re import findall
# text = "Google, Gooogle, Gooooole"
# match = findall(r'o{2,5}?', text)
# print(match)

#узнать знак года по индексу в списке
# lst = ["Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Заяц", "Дракон", "Змея", "Лошадь", "Овца"]
# year = int(input())
# result = year % 12
# print(lst[result])

#посчитать количество артиклей
# list_ = [i for i in input().lower().split() if i == 'an' or i == 'a' or i == 'the']
# print(f'Общее количество артиклей: {len(list_)}')

#ФИО
# name, second_name, otchestvo = input(), input(), input()
# print(f'{second_name[0].upper()}{name[0].upper()}{otchestvo[0].upper()}')

# str_ = input()
# b = 0
# a = 0
# for i in str_:
#     if i == "+":
#         b += 1
#     if i == '*':
#         a += 1
# print(b)
# print(a)


#поиск цифры в строке
# str_ = input()
# s = "Цифр нет"
# for i in range(len(str_)):
#     if str_[i] in '0123456789':
#         s = "Цифра"
#         break
# print(s)


#вывести сначала отр, потом 0, потом полож
# n = int(input())
# x = [int(input()) for _ in range(n)]
# [print(i) for i in x if i < 0]
# [print(i) for i in x if i == 0]
# [print(i) for i in x if i > 0]

# преобразование содержимого списка в Int
# print(*[int(i) ** 2 for i in input().split() if int(i) ** 2 % 10 != 4 and int(i) % 2 == 0])

#переставить местами min/max
# l = [int(i) for i in input().split()]
# x = l.index(min(l))
# y = l.index(max(l))
# l[x], l[y] = max(l), min(l)
# print(*l)


#строку превратить в число и каждую цифру возвести в куб
# palindromes = [int(i) ** 3 for i in input().split()]
# print(*palindromes, sep='\n')


#функции, map, reduce, filter
from functools import reduce
# number = int(input())
# str  = str(number)
# lst = list(map(int, str))
# result = list(map(lambda x: x*2, lst))
# less_than_10 = filter(lambda x: x<10, result)
# sum_result = reduce(lambda x,y: x+y, [1,2,3])
# print(int(sum_result))
# get_more_2 = [i+20 for i in result if i > 0]
# print(get_more_2)

#использование сразу трех функций в одной строке
# lst = []
# for i in range(int(input())):
#     digit = int(input())
#     lst.append(digit)
# def get_min(lst):
#     result = min(lst)
#     return result
# from functools import reduce
# a = filter(lambda x: x < 10, map(lambda x: x*2, [2, 3, 45, 345, 34]))
# df = list(a)
# print(df)
# print(get_min(df))

#использование map в функции
# lst_1 = [3,4,2,2,43,3]
# lst_2 = [3,24,24,24,24,24,4]
# def get_prod(a,b):
#     return a * b
# print(tuple(map(get_prod, lst_1, lst_2)))

#возведение в квадрат с помощью lambda
# lst_2 = [3,24,24,24,24,24,4]
# result = map(lambda x: pow(x,2), lst_2)
# print(tuple(result))

#ввести в список уникальные значения
# strings_list = []
# for i in range(int(input())):
#     a = input()
#     if a not in strings_list:
#         strings_list.append(a)
# print(strings_list)

#удалить max/min значения и вывести список
# number = int(input())
# lst = []
# for i in range(number):
#     digit = int(input())
#     lst.append(digit)
# lst.remove(max(lst))
# lst.remove(min(lst))
# print(*lst, sep="\n")

#интересное ДЗ, sep, lists, output
# number = int(input())
# lst_values = []
# lst_elements = []
# for i in range(1, number+1):
#     lst_elements.append(int(input()))
#     q = i*2
#     lst_values.append(q)
# print(*lst_elements, sep='\n')
# print()
# print(*lst_values, sep='\n')

#сложить элементы списка попарно
# number = int(input())
# count = 0
# lst = []
# #
# for i in range(number):
#     x = int(input())
#     count += x
#     lst.append(count)
#     x = count
# print(lst[1:])

#найти делители
# number = int(input())
# lst = []
# for i in range(1, number + 1):
#     if number % i == 0:
#         lst.append(i)
# print(lst)

# создать список list comprehension
# # print(list(range(1, int(input())+1)))
# # put your python code here
# number = int(input())
# a = [i for i in range(1, number+1)]
# print(a)

#создать список букв по их цифрам-номерам
# from string import ascii_lowercase
# number = int(input())
# print(list(ascii_lowercase[0:number]))


#создать список алфавит переменоженный
# from string import  ascii_lowercase
# print([char*index for index,char in enumerate(ascii_lowercase,1)])

#кубы из чисел
# number = int(input())
# lst = []
# for i in range(number):
#     num = int(input())
#     lst.append(pow(num, 3))
# print(lst)

#удалить нечетные индексы
# number = int(input())
# lst = []
# for i in range(number):
#     a = int(input())
#     lst.append((a))
# print(lst[::2])

#распаковка без for
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(*numbers)

