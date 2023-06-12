class Point:
    def __init__(self, coord_1 = 0, coord_2 = 0): #вызывается автоматически при создании объекта класса
        self.coord_1 = coord_1
        self.coord_2 = coord_2

    def move_to(self, new_x, new_y): #без __init__ метод нужно вызывать вручную
        self.x = new_x
        self.y = new_y

    def go_home(self):
        self.x = 0
        self.y = 0

P1 = Point()
print(P1.go_home())



Point_1 = Point(3, 34)
Point_2 = Point(-3, 34)
Point_3 = Point()
Point_3.move_to(34, 23)













# class Cat:
#     # color = 'blue'
#     # def set_value(self, value, age=0):
#     #     self.name = value
#     #     self.age = age
# # __init__ это магический метод. позволяет инициализировать объект, не нужен set_value
#
#     def __init__(self, name, breed='pers', age=1, color='blue'):
#         print('Hello, cat', self, name, breed, age, color)
#         self.name = name
#         self.age = age
#         self.breed = breed
#         self.color = color
#
# walt = Cat("Walt")

