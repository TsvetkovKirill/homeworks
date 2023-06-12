import json
data = {'president': {'name': 'Joe Biden', 'species': 'homo'}}
with open(r'C:\Users\29\PycharmProjects\homeworksPython\open_read_and_write_in_files\new.json', 'w', encoding ='utf-8') as write_file:
    json.dump(data, write_file)

json_string = json.dumps(data)
print(type(json_string))

import json

d = {'абв': 1, 'где': 2, 'ёжз': 3}

with open(r'C:\Users\29\PycharmProjects\homeworksPython\open_read_and_write_in_files\data.json', 'w', encoding='utf-8') as file:
    json.dump(d, file, ensure_ascii=False, indent = 4)






#запись в файл бинарный формат
# import pickle
# books = [
#     ("Евгений Онегин", "Пушкин А.С.", 200),
#     ("Муму", "Тургенев И.С.", 250),
#     ("Мастер и Маргарита", "Булгаков М.А.", 500),
#     ("Мертвые души", "Гоголь Н.В.", 190)
# ]
# # file = open('out.bin', 'wb')
# # pickle.dump(books, file)
#
# file = open('out.bin', 'rb')
# tuple_ = pickle.load(file)
# file.close()
# print(tuple_)


# import csv

#чтение данных из файла
# try:
#     with open(r'C:\Users\29\PycharmProjects\homeworksPython\open_read_and_write_in_files\text.txt', 'a+', encoding='utf-8') as f:
#         f.seek(0)
#         add_write = f.writelines(["Fuck off"])
#         s = f.readlines()
#         print(*s)
# except FileNotFoundError:
#     print("невозможно открыть файл")
# except:
#     print("ошибка при работе с данными.")

#запись данных в файл
# try:
#     with open('new_file.txt', 'a+', encoding='utf-8') as new_f:
#         new_f.seek(0)
#         new_f.writelines(["Fuck all of you, fucking transgender\n", "and what now\n"])
#         # s = new_file.readlines()
#         s = new_f.readlines()
#         print(s)
# except:
#     print("Ошибка в момент формирования твоей зиготы")




# f = open('file.txt', 'rt')
# f = open('file.txt', 'r')
#считываем весь файл read
# f = open(r'C:\Users\29\PycharmProjects\homeworksPython\open_read_and_write_in_files\text.txt', encoding = 'UTF-8')
# for i in f:
#     print(i, end = '')
# print(f.read())#можно передавать параметры
# print(type(f))
# print(f.readline(), end = '')
# print(f.readline())
# f.seek(0)#вернуться к выбранному индексу и начать с него
# f.close()

#считываем отдельные строки в файле
# f = open('text.txt')
# result = f.readline()
# result_2 = f.readline()
# print(result_2)
# print(result_2)
#
# print(type(result))
# f.close()

# считываем строки в виде списка
# f = open('text.txt')
# result = f.readlines()
# print(' '.join(result), sep = " ")
# print(type(result))
# # f.close()

#записывать строки по очереди
# f = open('text.txt', 'w', encoding='utf-8')
# f.write("Привет, коллеги\n")
# f.write("Fuck yous colleages!")
# f.close()

#записываем сразу несколько строк
# f = open('C:\Users\29\PycharmProjects\homeworksPython\open_read_and_write_in_files\text.txt', 'w')
# f.writelines(['Hello world\n', 'Fuck off\n'])
# f.close()

# writer = csv.writer(f, quoting=csv.QUOTE_NONE, escapechar='\\', delimiter=';')
#
# with open(r'C:\Users\29\PycharmProjects\homeworksPython\open_read_and_write_in_files\new_file.txt') as f:
#     reader = csv.DictReader(f)
#     count = 0
#     for row in reader:
#         print(row['title'])
#         count += 1
#
# print(f"Всего {count} ................")
#

