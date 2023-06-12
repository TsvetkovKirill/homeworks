# class Line:
#     def __init__(self, a, b, c, d):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.d = d
#
# class Rect:
#     s = 'Ya'
#     def __int__(self, a, b, c, d):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.d = d



# # print(Rect.__dict__)
# print(getattr(Rect, 's', False))
# setattr(Rect, 'element', 200)
# print(Rect.element)
# print()
# lst = [10, -5, 100, 20, 0, 80, 45, 2, 5, 7]
# print(*(sorted([i for i in lst if 0 <= i <= 10])))
# class Graph:
#     LIMIT_Y = [0, 10]
#
#     def set_data(self, data):
#         self.data = data
#
#     def draw(self):
#         print()
#
# graph_1 = Graph()
# graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
# graph_1.draw()

# class MediaPlayer:
#     def open(self, file):
#         self.filename = file#создали локальный атрибут filename со значением file
#     def play(self):
#         print(f"Воспроизведение медиа-файла {self.filename}")
# media1 = MediaPlayer()
# media1.open('filemedia1')
# media2 = MediaPlayer()
# media2.open('filemedia2')
# media1.play()
# media2.play()




# class Person():
#     name = "Сергей Балакирев"
#     job = "Программист"
#     city = "Москва"
# p1 = Person()
# # hasattr(p1, 'job')#существует ли локальное свойство в классе? выведет True or False проверяем именно локально!
# # if p1 == True:
# #     print(True)
# # else:
# #     print(False)
# p1.name = "Kirya"
# print(getattr(Person, 'nam', False))


 # Есть ли у объекта локальное свойство с именем job
# class Person():
#     name = "Сергей Балакирев"
#     job = "Программист"
#     city = "Москва"
#     def set_coords(self):
#         print("вызов" + str(self))
# #
#
# p1 = Person()
# p1.set_coords()
# hasattr(p1, 'job')
# if p1 == True:
#     print(True)
# else:
#     print(False)
# Person.set_coords(p1)

# class Point:
#     color = 'red'
#     circle = 2
# Point.color = "black"#новое значение для атрибута класса
# Point.__dict__#увидеть список всех атрибутов класса
# a = Point()#создали объект класса
# a.color = 'green'#присвоить атрибуту экземпляра класса a новое значение. Это пространство имен именно объекта a
# print(a.__dict__)#увидеть список атрибутов именно объекта a
# Point.size = 'big'#создали новый атрибут класса и присвоили ему значение
# setattr(Point, 'volume', 14)#создали новый атрибут класса и присвоили ему значение (как в прошлой строке)
# setattr(a, 'number', 10)
# print(Point.color)#получить значение атрибута класса. также работает с объектами класса
# print(a.color)
# print(getattr(Point, 'color', False))#если атрибута нет, выведет False, если есть - выведет значение атрибута
# del Point.color#удалить атрибут из пространства имен. работает и для объектов
# delattr(Point, 'color')#удалить атрибут, как в прошлом примере
# print(hasattr(Point, 'age'))#получить свойство. Если его нет, выведет False


# class Figure():#объявили класс
#     type_fig = 'ellipse'#определили атрибут класса и присвоили ему значение
#     color = 'red'
# fig1 = Figure()#объявили объект/экземпляр класса
# setattr(fig1, 'start_pt', (10, 5))#добавили локальный атрибут объекта и присвоили ему значение
# setattr(fig1, 'end_pt', (100, 20))
# setattr(fig1, 'color', 'blue')
# delattr(fig1, 'color')#удалили атрибут объекта
# print(*fig1.__dict__)#распаковали, получили только ключи, составляющие список доступных атрибутов


# class Car:
#     pass
#
# setattr(Car, 'model', 'Тойота')#добавить новый атрибут
# setattr(Car, 'color', 'Розовый')
# setattr(Car, 'number', 'П111УУ77')
# print(Car.__dict__['color'])#получить значение атрибута
# class Dictionary:
#     rus = "Питон"
#     eng = "Python"
# print(getattr(Dictionary, 'eng'))
# print(getattr(Dictionary, 'rus_word', False))#чтобы избежать ошибки. Вернет False, если аргумент не найден

# class TravelBlog():
#     total_blogs = 0
# tb1 = TravelBlog()#создали объект/экземпляр класса TravelBlog
# tb1.name = "Франция"
# tb1.days = 6
# TravelBlog.total_blogs += 1
# tb2 = TravelBlog()
# tb2.name = "Италия"
# tb2.days = 5
# TravelBlog.total_blogs += 1
