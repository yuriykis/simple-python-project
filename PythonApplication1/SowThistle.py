from tkinter import*
from World import*
from Coords import*
from Organism import*
from random import*
from Plant import*


class SowThistle(Plant):
   def __init__(self, world, name, strength, location, color):
       return super().__init__(world, name, strength, location, color)

   def action(self, fields, canvas, side):
        r = randrange(50)
        if(r == 2):
            for i in range(3):
                canvas = self.multiply(fields, canvas);
        return canvas


