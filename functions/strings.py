



# str_ = input()
# last_symbols = str_[-1]
# lst = list(str_)
# del lst[-1]
# a = ''.join(lst)
# print(f'{last_symbols}{a}')


# number = int(input())
# def get_str(number):
#     for i in range(0, number):
#         str_ = input()
#     return str_
# print(type(get_str(number)))



# lst = [['kjhjk'], ['qqqqqqqqqq'], ['iiiiiiiiiiiii']]
# extend_list = []
# for i in lst:
#     extend_list.extend(i)
#     sorted_list = sorted(extend_list)
# print(sorted_list)



# s = input()                # Получаем строку
#
# a = s.find('h')            # Индекс первого вхождения
# b = s.rfind('h')           # Индекс последнего вхождения
# c = s[a:b+1]               # Получаем текст между начальным и конечным индексом
# print(s.replace(c, ''))


# number = int(input())
# for i in range(number+1):
#     a = i * i
#     print(f"Квадрат числа {i} равен {a}")



#показать индексы по условиям
# str_ = input()
# if str_.count('f') == 1:
#     print(str_.find('f'))
# elif str_.count('f') >= 1:
#     print(str_.find('f'), end = ' ')
#     print(str_.rfind('f'), end = ' ')
# elif 'f' not in str_:
#     print("NO")


#посчитать самый частовстречающийся символ
# from collections import Counter
# c = Counter(input())
# print(c.most_common(1)[0][0])


# s = input()
# max_count = 0
# max_char = ''
# for i in range(len(s)):
#     if s.count(s[i]) >= max_count:
#         max_count = s.count(s[i])
#         max_char = s[i]
# print(max_char)

#посчитать количество 11 больше 3
# number_stings = int(input())
# three_count = 0
# for i in range(number_stings):
#     s = input()
#     if s.count('11') >= 3:
#         three_count += 1
# print(three_count)

#проверить, какой символ в конце
# str_ = input()
# if str_.endswith('.ru') or str_.endswith('.com'):
#     print("YES")
# else:
#     print("NO")

#посчитать количество вхождений в строке
# from re import findall
# str_ = input()
# aA = len(findall(r"[аА]", str_))
# gG = len(findall(r"[гГ]", str_))
# cC = len(findall(r"[цЦ]", str_))
# tT = len(findall(r"[тТ]", str_))
# print(f"Аденин: {aA}")
# print(f"Гуанин: {gG}")
# print(f"Цитозин: {cC}")
# print(f"Тимин: {tT}")

#найти все символы в нижнем регистре
# word = input()
# symbols = []
# for i in word:
#     if i.isalpha() == True:
#         symbols.append(i)
# a = ''.join(symbols)
# count = 0
# for b in a:
#     if b.islower() == True:
#         count += 1
# print(count)
#
# s = input()                   # Исходная строка
# k = 0                         # Количество буквенных символов в нижнем регистре
#
# for i in range(len(s)):       # Цикл по длине
#     if s[i] != s[i].upper():  # Если символ не равен символу в верхнем регистре
#         k+=1                  # Добавляем +1 к кол-ву
# print(k)

#вывод каждого второго элемента по индексу
# s = input()
# for c in range(0, len(s), 2):
#     print(s[c])

#вывести элементы в стоблик в обратном порядке
# s = input()
# for c in reversed(s):
#     print(c)

#вывести инициалы
# name, second_name, otchestvo = input(), input(), input()
# print(f'{second_name[0].upper()}{name[0].upper()}{otchestvo[0].upper()}')

#наличие цифр в строке
# digit = input()
# result = "Цифр нет"
# for i in digit:
#     if i.isdigit():
#         result = "цифра есть"
#     else:
#         result
# print(result)

#сравнение соседних символов
# str_ = input()
# count = 0
# for i in range(len(str_) -1):
#     if str_[i] == str_[i + 1]:
#             count += 1
# print(count)

#посчитать гласные и согласные в строке
# from re import findall
# str_ = input()
# vowels = len(findall(r"[ауоыиэяюёеАУОЫИЭЯЮЁЕ]", str_))
# consonants = len(findall(r"[бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ]", str_))
# print(f"Количество гласных букв равно {vowels}")
# print(f"Количество согласных букв равно {consonants}")

#переводи из десятичной в двоичную систему счисления
# a = 12341
# b3 = format(a, 'b')
# print(b3)

#удалить элемент из строки по индексу
# word = input()
# print(word[2])
# print(word[-2])
# print(word[0:5])
# print(word[0:-2])
# print(word[0::2])
# print(word[1::2])
# print("".join(reversed(word)))
# print(word[::-2])

#выебоны автора курса
# s = input()
# x = len(s)
# a = x // 2 + x % 2
# print(s[a:] + s[:a])

#проверка на первую заглавную букву istitle
# word = input()
# if word.istitle() == True:
#     print("YES")
# else:
#     print("NO")

