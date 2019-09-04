from tkinter import*
from World import*
from Coords import*
from Organism import*
from Animal import*

class Human(Animal):

    def __init__(self, world, name, strength, location, color):
        return super().__init__(world, name, strength, location, color)
    
    def action(self, fields, canvas, side):
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