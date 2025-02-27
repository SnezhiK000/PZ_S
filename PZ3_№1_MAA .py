'''
ЗАДАНИЕ 1
'''

class Human: #класс человек
    def __init__(self,head,body,hands,legs,height):
        self.__head = head
        self.__body = body
        self.__hands = hands
        self.__legs = legs
        
        #Получение полей головы
    def get_head(self):
        return self.__head
    
    def set_head(self, head):
        self.__head = head
        
        
        #Получение полей тела
    def get_body(self):
        return self.__body
    
    def set_body(self, body):
        self.__body = body  
          
        #Получение полей рук  
    def get_hands(self):
        return self.__hands
    
    def set_hands(self, hands):
        self.__hands = hands   
        
        #Получение полей ног
    def get_legs(self):
        return self.__legs
    
    def set_legs(self, legs):
        self.__legs = legs     


              
                