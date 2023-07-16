# #первая задача
# number_ = int(input())
# count = 1
# digit = 2
# while digit < number_:
#     count += 1
#     digit *= 2
# if digit == number_:
#     print(count)
# elif number_ == 1:
#     print(0)
# else:
#     print("НЕТ")
#
# #вторая задача
# number_ = int(input())
# first_digit = int(str(number_)[0])
# while first_digit != 1 and number_ <= 1000000000:
#     number_ = number_ * first_digit
#     first_digit = int(str(number_)[0])
# print(number_)

# третья задача
# b = ''
# while True:
#     a = input()
#     if 5 <= len(a) <= 9:
#         b = a
#     else:
#         break
# print(b)
# def get_numbers(number_1: int, number_2: int) -> int:
#     x = number_1
#     while x >= number_1 and x <= number_2:
#         if x % 2 == 0 or x % 3 == 0:
#             continue
#         elif x % 777 == 0:
#             break
#         x = number_1 + 1
#
#     return x
# print(get_numbers(int(input()), int(input())))
a=-1
while a<=b:
    a+=1
    if a%777==0:
        break
    if a%2==0 or a%3==0:
        continue
    print(a)