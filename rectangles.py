class Rectangle :
   def __init__(self , length , width , height) -> None:
      self.length = length
      self.width = width
      self.height = height
      try :
         if int(self.length) < 0  or int(self.width) < 0  or int(self.height) < 0  :
            raise ValueError
      except ValueError:
         raise ValueError
   def calculate_volume(self):
       return (self.length * self.width) * self.height
      