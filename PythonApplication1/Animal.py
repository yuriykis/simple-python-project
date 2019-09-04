from tkinter import*
from World import*
from Coords import*
from Organism import*
from random import*

class Animal(Organism):
    def __init__(self, world, name, strength, location, color):
        return super().__init__(world, name, strength, location, color)

    def action(self, fields, canvas, side):
        r = randrange(4)
        if(r == 0):
            side = 'Right'
        elif(r == 1):
            side = 'Left'
        elif(r == 2):
            side = 'Up'
        elif(r == 3):
            side = 'Down'

        if(side == 'Right'):
           if((self.location.x + 40)/40 < 20):
            new_coords = Coords((self.location.x + 40)/40, (self.location.y)/40)
           else:
               return canvas
        elif(side == 'Left'):
           if((self.location.x + 40)/40 > 1):
            new_coords = Coords((self.location.x - 40)/40, (self.location.y)/40)
           else:
               return canvas
        elif(side == 'Up'):
           if((self.location.y + 40)/40 > 1):
            new_coords = Coords((self.location.x)/40, (self.location.y - 40)/40)
           else:
               return canvas
        elif(side == 'Down'):
           if((self.location.y + 40)/40 < 20):
            new_coords = Coords((self.location.x)/40, (self.location.y + 40)/40)
           else:
               return canvas

        canvas = self.move(new_coords, fields, canvas)
        return canvas

    def move(self, new_coords, fields, canvas):
        org = self.world.check_field(new_coords)
        if org == None:
            canvas =  self.draw_empty(fields, canvas)
            self.set_location(new_coords)
            canvas = self.draw_organism(fields, canvas)
            return canvas
        else:
            canvas = self.colision(self, org, fields, canvas)
            return canvas

        


