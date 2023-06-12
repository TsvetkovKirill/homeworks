from bs4 import BeautifulSoup
import requests
r = requests.get('https://hentai-monster.art/cosplay/cosplay-26')
image = requests.get('https://hentai-monster.art/uploads/cosplay/21/417_hentai-monster.art.jpg')
with open('new_ero_photo.jpg', 'wb') as f:
    f.write((image.content))
import requests
from bs4 import BeautifulSoup


class HabrPythonNews:

    def __init__(self):
        self.url = 'https://habr.com/ru/hub/python/'
        self.html = self.get_html()

    def get_html(self):
        try:
            result = requests.get(self.url)
            result.raise_for_status()
            return result.text
        except(requests.RequestException, ValueError):
            print('Server error')
            return False

    def get_python_news(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        news_list = soup.findAll('h2', class_='post__title')
        return news_list


if __name__ == "__main__":
    news = HabrPythonNews()
    print(news.get_python_news())


# str_ = input().lower()
# remove_elements = ['.', ',', '!', '?', ':', ';', '-']
# for char in remove_elements:
#     if char in str_:
#         str_ = str_.replace(char, '')
# lst_ = str_.split()
# dict = {}
#
# for i in lst_:
#     dict[i] = dict.get(i, 0) + 1
#
# min_val = min(dict.values())
# # resulst = []
# resulst_lst = []
# for k, v in dict.items():
#     if v == min_val:
#         resulst_lst.append(k)
# print(min(resulst_lst))

# number = int(input())
# if number < 1000:
#     print(number)
# else:
#     print('{0:,}'.format(number).replace(',', ','))

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
# # def get_name(doc_number):
# #     for data in documents:
# #         if data.get("number") == doc_number:
# #             return data.get('name')
# #             return 'Документ не найден'
#
#
# def get_directory(doc_number):
#     for data in directories:
#         if doc_number in directories.get(data):
#             return data
#         else:
#             return "нет такого"
#
#
# # your code
#
# # def add(document_type, number, name, shelf_number):
# #     if shelf_number not in directories:
# #         return 'Нет такой полки'
# #     doc = {}
# #     for info in ('type', 'number', 'name'):
# #         doc[info] = document_type, number, name
# #         directories[shelf_number] = directories.get(shelf_number).append(doc['number'])
# #     return 'Документ добавлен'
# # print(documents)
# #
# if __name__ == '__main__':
#     # print(get_name("10006"))
#     # print(get_directory("11-2"))
#     # print(get_name("101"))
#     add('international passport', '311 020203', 'Александр Пушкин', 3)
#     # print(get_directory("311 020203"))
#     # print(get_name("311 020203"))
#     # print(get_directory("311 020204"))
#
#
#
# # counter = 0
# # lst = []
# # for i in range(3):
# #     a = int(input())
# #     if a > 10:
# #         counter += 1
# #     else:
# #         lst.append(a)
# # print(f"Меньше 10 {' '.join(str(lst))} ")
# # print(counter)
#
#
# # sum = 0
# # text = input()
# # # a = int(input())
# # while text != 'stop':
# #     a = int(text)
# #     sum += a
# #     text = input()
# # print(sum)
#
#
# # text = input()
# while text != "КОНЕЦ":
#     print(text)
#     text = input()
