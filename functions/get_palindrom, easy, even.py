
# def check_password(is_palindrome, is_simple_number, is_even):
#     a = is_palindrome
#     b = is_simple_number
#     c = is_even
#     # if a == True and b == True and c == True:
#         return True
def is_palindrome(str_):
    first_colon = str_.find(":")
    first_number = str_[:first_colon]
    return first_number == first_number[::-1]


def is_simple_number(str_):
    a = ":"
    indexes = [i for i, c in enumerate(str_) if c == a]
    a = indexes[0]
    b = indexes[1]
    simple_number_str = str_[a+1:b]
    simple_number_digit = int(simple_number_str)
    if simple_number_digit <= 1:
        return False
    else:
        for i in range(2, simple_number_digit):
            if simple_number_digit % i != 0:
                return True

def is_even(str_):
    last_colon = str_.rfind(":")
    third_number = str_[last_colon+1:]
    number = int(third_number)
    return number % 2 == 0


str_ = input()
# print(is_palindrome(str_))
# print(is_even(str_))
# print(is_simple_number(str_))
# print(check_password(is_palindrome(str_), is_simple_number(str_), is_even(str_)))
if is_even(str_) == True and is_palindrome(str_) == True and is_simple_number(str_) == True:
    print("True")
else:
    print("False")