from tkinter import*
from World import*
from Coords import*
from Organism import*
from random import*


class Plant(Organism):
    def __init__(self, world, name, strength, location, color):
        return super().__init__(world, name, strength, location, color)

    def action(self, fields, canvas, side):
        r = randrange(50)
        if(r == 2):
            canvas = self.multiply(fields, canvas);
        return canvas
