#! /usr/bin/env python3
# В python утиная типизация

# class my_class (parent1, parent2,...):
#   def __init__(self): # контсруктор. self- ссылка на себя
#       pass
#   def my_method(self):
#       attr1 = 0       # attr1 - ститическая переменная 
#       self.attr = 1   #- есть во всех экземплярах

# p.__init__(self) конструктор
# p.__str__(self)  преобразование в стоку при prinf
# p.__repr__(self) преобразование в строку при работе интерпретатора
# p.__del__(self)  финализатор.

# Python удаляет объекты которые недоступны из стека вызовов.

# Особые варианты название для методов
# _attribute
# __attribute
# __attribute__

# Чтобы скрыть как
class my_calss(object):
    """docstring for ClassName"""
    def __init__(self, arg):
        super(my_class, self).__init__()
        self.a = arg
        

def main():
    

if(__name__ == "__main__"):
    main()
