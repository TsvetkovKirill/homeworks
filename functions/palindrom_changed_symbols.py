
def is_palindrome(str_, replaced_symbols):
    for i in replaced_symbols:
        old, new = i
        str_ = str_.lower().replace(old, new)
    return str_ == str_[::-1]



str_ = input()
replaced_symbols = [(',', ''), ('.', ''), ('!', ''), ('?', ''), ('-', ''), (' ', '')]
print(is_palindrome(str_, replaced_symbols))

# str_ = input()
# replaced_symbols = [(',', ''), ('.', ''), ('!', ''), ('?', ''), ('-', '')]
# # print(is_palindrome(str_, replaced_symbols))
# # def is_palindrome(str_, replaced_symbols):
# for i in replaced_symbols:
#     old, new = i
#     str_ = str_.replace(old, new)
#     # print(str_)
#     # print(str_[::-1])
# if str_ == str_[::-1]:
#     print(True)
# else:
#     print(False)
