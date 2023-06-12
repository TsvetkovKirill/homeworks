# documents = [
#         {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
#         {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
#         {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
#         {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
#       ]
#
# directories = {
#         '1': ['2207 876234', '11-2', '5455 028765'],
#         '2': ['10006'],
#         '3': []
#       }
#
# def get_name(doc_number):
#     for data in documents:
#         if data.get("number") == doc_number:
#             return data.get('name')
#             return 'Документ не найден'
#
#
# def get_directory(doc_number):
#     for data in directories:
#         if doc_number in directories.get('data'):
#             return data
#             return "нет такого"
#
# # your code
#
# def add(document_type, number, name, shelf_number):
#     # shelf = input('Введите номер полки куда положить документ. ')
#     if shelf_number not in directories:
#         return 'Нет такой полки'
#     doc = {}
#     directories[shelf] = directories.get(shelf).append(doc['number'])
#     return 'Документ добавлен'
# #
# if __name__ == '__main__':
#     print(get_name("11-2"))
#     print(get_directory("11-2"))
#     # print(get_name("101"))
#     # add('international passport', '311 020203', 'Александр Пушкин', 3)
#     # print(get_directory("311 020203"))
#     # print(get_name("311 020203"))
#     # print(get_directory("311 020204"))










# from math import sqrt

# print("Введите коэффициенты для уравнения")
# print("ax^2 + bx + c = 0:")
# a = float(input("a = "))
# b = float(input("b = "))
# c = float(input("c = "))
#
# discr = b ** 2 - 4 * a * c
# print("Дискриминант D = %.2f" % discr)
#
# if discr > 0:
#     x1 = (-b + math.sqrt(discr)) / (2 * a)
#     x2 = (-b - math.sqrt(discr)) / (2 * a)
#     print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
# elif discr == 0:
#     x = -b / (2 * a)
#     print("x = %.2f" % x)
# else:
#     print("Корней нет")

# def get_avg_ex_grade(students):
#     sum_ex = 0
#     for student in students:
#         sum_ex += student['exam']
#         return round(sum_ex / len())

lst = ['Lidia', 'Masha', 'Sveta', 'Irina']
print(lst.pop(2))
print(lst)