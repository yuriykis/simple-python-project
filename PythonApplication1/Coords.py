from World import*

class Coords(object):

   def __init__(self, x, y):
      self.x = 40*x
      self.y = 40*y

   def set_coords(self, x, y):
       self.x = x
       self.y = y

   def is_equal(self, x, y):
       if ((self.x == x) & (self.y == y)):
           return TRUE


