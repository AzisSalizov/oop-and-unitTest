import unittest
from rectangles import Rectangle
from unittest import main

# Задание 1
# Создайте класс. Добавьте к классу 3 параметра. Напишите 1 метод, который будет выводить на экран все 3 параметра. Создайте экземпляр класса. Вызовите его метод

# class Person:
#    def __init__(self , name , age , btd) -> None:
#       self.name = name
#       self.age = age
#       self.btd = btd
      
#    def __str__(self) -> str:
#       return f'Меня зовут {self.name}\nМне {self.age} лет\nРодился {self.btd} июня'

# person = Person('Azis' , 18 , 6)
# print(person)



# Задание 2
# Вам дан класс:class Monkey:
#     max_age = 12
#     loves_bananas = True

#     def climb(self):
# 	print('I am climbing the tree') 
# Создайте 2 экземпляра данного класса. У каждого экземпляра вызовите оба параметра описанные в этом классе. Для обоих экземпляров вызовите метод climb


# class Monkey:
#    max_age = 12
#    love_bananas = True
   
#    def climb(sefl) :
#       print('I am climbing the tree')
      
#    def __str__(self) -> str:
#       return f'Лет {self.max_age}\nКушать {self.love_bananas}'
      
   
# monkey = Monkey()
# tiger = Monkey()
# hyena = Monkey()
# monkey.climb
# tiger.climb
# hyena.climb
# print(monkey.max_age , monkey.love_bananas)
# print(tiger.max_age , tiger.love_bananas)
# print(hyena.max_age , hyena.love_bananas)


# Задание 3
# Создайте класс Person. При создании экземпляра данного класса мы должны вводить 3 парамметра name, age, gender.
# Напишите метод calculate_age к этому классу, этот метод должен принимать в себя число и возвращать в каком возрасте будет человек через это число лет.

# Пример:
# p = Person('John', 23, 'male')
# p.calculate_age(10)


# class Person:
#    def __init__(self , name , age , gender) -> None:
#       self.name = name
#       self.age = age
#       self.gender = gender
   
#    def calculate_age(self , num):
#       self.num = num
      
#    def __str__(self) -> str:
#       if self.num :
#          return f'Меня зовут {self.name}\nМне {self.age + self.num} лет\nПол {self.gender}'
#       else :
#          return f'Меня зовут {self.name}\nМне {self.age} лет\nПол {self.gender}'
   
# person = Person('Azis' , 18 , 'Мужской')
# person.calculate_age(12)
# print(person)

class TestCubes (unittest.TestCase):
   def test_init(self):
    c = Rectangle(5, 3, 10)
    self.assertEqual(c. length, 5)
    self.assertEqual(c.width, 3)
    self.assertEqual(c.height,10)
   def test_init_raise(self):
      with self.assertRaises(ValueError):
        c = Rectangle('Length', (1, 2, 3) , {4: 5})
   def test_negative_value (self):
      with self.assertRaises(ValueError) as context:
       c = Rectangle(-1, 2, 6)
   def test_volume_calculation(self):
      c = Rectangle(5, 4, 7)
      self.assertEqual(c.calculate_volume(), 140)

if __name__ == '__main__':
   main()