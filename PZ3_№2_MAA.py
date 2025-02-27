'''
ЗАДАНИЕ 2
1 задать размер головы окружностью, будет принимать значения a,b,c,d формула: (a+b)/2 и (b+d)/2 (А;B). Такии образом длина от А до B это высота и ширина головы(?)
2 теловище: координата верхнего левого угла(и всех в принципе) и ширина-высота 
3 руки: задаются длинами и углами положения из верхних углов
4 ноги: задаются длинами и углами положения из нижних углов
5:функция оперделения роста человека
'''
class Human: #класс человек
    def init(self):
        self.head = 0
        self.body = 0
        self.hands = 0
        self.legs = 0
        self.height = 0
        
    def body(self,body):
        self.body = body
    
    def head(self,head):
        self.head = head   
    
    def hands(self, hands):
        self.hands = hands
        
    def legs(self,legs):
        self.legs = legs
        
    def height (self, height):
        self.height = height
              
                
human = Human() #создаем новый объект Человек

horizont = float(input("Введите ширину тела: "))
wertical = float(input("Введите длинну тела: "))
leftUp = float(input("Введите точку верхнего левого угла: ")) #ввод точки верхнего левого угла
rightUp = float(leftUp + horizont) #точка правого верхнего угла

print("Введите конечные точки радиуса, где начало и середина окружности(a.b), а конец (c.d)")
a = float(input("Введите точку a.b: "))
b = float(input("Введите точку c.d: "))
if a > b:
    head = 2*(a-b)
else:
    head = 2*(b-a)

hands = float(input("Введите длину рук: "))

#СГИБАНИЕ ПЛЕЧА
shouldersC = float(input("Введите градус сгибания плеча (не более 15):  "))

while shouldersC >15 or shouldersC < 0:
    if shouldersC <=15 and  shouldersC > 0:
        shouldersC = float(input())
       
    if shouldersC > 15 or shouldersC <= 0:
        shouldersC = float(input("Введите меньший градус: "))
    
    if shouldersC <= 0:
        a = input("Введите больший градус: ")
        print(f"Введено: {a}")
        shouldersC = float(a)

#ЛОКТЕВОЙ СУСТАВ
insideC = float(input("Введите уградус лоектвого сустава (не более 120): "))

while insideC >120 or insideC < 0:
    if insideC <=120 and insideC > 0:
        insideC = float(input())
       
    if insideC > 120:
        insideC = float(input("Введите меньший градус: "))
        
    if insideC <= 0:
        insideC = float(input("Введите больший градус: "))



legs = float(input("Введите длину ног: "))

#ТАЗОБЕДРЕННЫЙ СУСТАВ
legC = float(input("Введите градус сгибания тазобедренного сустава (не более 250):  "))

while legC >250 or legC < 0:
    if legC <=250 and legC > 0:
        legC = float(input())
       
    if legC > 250:
        legC = float(input("Введите меньший градус: "))
    
    if legC <= 0:
        legC = float(input("Введите больший градус: "))
  

#СГИБАНИЕ КОЛЕНА
insideC = float(input("Введите уградус сгибания колена (не более 140): "))

while insideC > 140 or insideC < 0:
    if insideC <=140:
        insideC = float(input())
       
    if insideC > 140 or insideC <= 0:
        insideC = float(input("Введите меньший градус: "))
        
    if insideC <= 0:
        insideC = float(input("Введите больший градус: "))    
    

human.head(head)
human.hands(hands)
human.legs(legs)
human.body(wertical) #Записываем длину тела человека

height = human.body + human.head + human.legs

print(f"Рост человека: {height}")
print(f"Длина рук человека: {hands}")
print(f"Длина ног человека: {legs}")
print(f"Длина головы человека: {head}")

