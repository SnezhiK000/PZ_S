import math
'''
# №1
class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        s = math.pi * self.radius ** 2
        print (f"Площадь радиуса {self.radius} равна: {s}")
        
    def circumference(self):
        length = 2*self.radius * math.pi
        print(f"Длинна окружности {length}")

circle_one = Circle(5)

circle_one.area()
circle_one.circumference()


# №2
people = [("Маруся",18), ("Алла", 14), ("Яшма", 15)]

list_name_age = sorted(people, key=lambda person: person[1])
print(f"Отсортированный список по возрасту: {list_name_age}")



words = ["Алина", "Люда", "Рита", "Ева", "Ульяна", "Женя", "Ольга", "Яшма"]
people_words = list(filter(lambda word: word[0] in "АИЭЕУЮОЯ", words))

print(f"Слова, начинающиеся с гласной буквы: {people_words}")



# №3
class Student:
    def __init__(self, name):
        self.__name = name
        self.__marks = [] 
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
    
    def get_marks(self):
        return self.__marks
    
    def add_grade(self):
        marks_input = input("Введите оценки ученика: ")
        marks_list = [int(mark) for mark in marks_input.split(",")]
        self.__marks.extend(marks_list)
    
    def average_grade(self):
        if not self.__marks:
            return 0
        return sum(self.__marks) / len(self.__marks)


student_one = Student("Nastya")
student_one.add_grade()
print(f"Средняя оценка {student_one.get_name()}: {student_one.average_grade()}")
'''
# №4
class Polygon:
    def __init__(self):
        self = self

    def area(self):
        return 0
    
    def perimeter(self):
        return 0
    
class Rectangle(Polygon):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return self.width + self.height
    
class Triangle(Polygon):
    def area(self):
        return 
    
    def perimeter(self):
        return 
    
one = Rectangle()
two = Triangle()