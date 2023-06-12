#вывести True, если все слова одинаковой длины и отличаются на один символ
# def is_one_away(word1, word2):
#     if len(word1) != len(word2):
#         return False
#     count = 0
#     for i in range(len(word1)):
#         if word1[i] != word2[i]:
#             count += 1
#         if count == 1:
#             return True
#         return False
#
# word1 = input()
# word2 = input()
# print(is_one_away(word1, word2))




#хороший пароль
# def is_password_good(password):
#     good_pass = 0
#     if len(password) >= 8:
#         good_pass += 1
#     for i in password:
#         if i.isupper():
#             good_pass += 1
#             break
#     for j in password:
#         if j.islower():
#             good_pass += 1
#             break
#     for k in password:
#         if k.isdigit():
#             good_pass += 1
#             break
#     if good_pass == 4:
#         return True
#     else:
#         return False

# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(is_password_good(txt))
#
# password = input()



#найти просто число
# def is_prime(num):
#     if num == 1:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(is_prime(n))


# считываем данные
# n = int(input())
#
# # вызываем функцию
# print(is_prime(n))
