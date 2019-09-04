from tkinter import*
from Coords import*

class Field():

    def __init__(self, coords):
        self.coords = coords

    def draw_field(self, c):
       c.create_rectangle((self.coords.x, self.coords.y, self.coords.x + 40, self.coords.y + 40), fill="silver", outline='silver')
       return c

    def change_field(self, c, color):
       c.create_rectangle((self.coords.x, self.coords.y, self.coords.x + 40, self.coords.y + 40), fill = color, outline = color)

