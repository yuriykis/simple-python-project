from tkinter import*
from World import*
from Coords import*
from Organism import*
from random import*
from Plant import*

class Grass(Plant):
   def __init__(self, world, name, strength, location, color):
       return super().__init__(world, name, strength, location, color)

