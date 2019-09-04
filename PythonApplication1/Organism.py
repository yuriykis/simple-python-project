from tkinter import*
from World import*
from Coords import*

class Organism(object):
    
    def __init__(self, world, name, strength, location, color):
        self.name = name
        self.strength = strength
        self.location = location
        self.world = world
        self.color = color

    def action(self):
        return

    def get_strength(self):
        return self.strength

    def multiply(self, fields, canvas):
        coords = self.world.free_random(self.location)
        if(coords.is_equal(self.location.x, self.location.y)):
            return canvas
        canvas = self.world.update_canvas(canvas)
        self.world.add_organism(coords, self.get_name())
        print(self.name, end = ' ')
        print('was multiplied!')
        return canvas
        

    def kill(self, fields, canvas):
        canvas = self.draw_empty(fields, canvas)
        self.world.delete_organism(self.location)
        return canvas

    def colision(self, attacker, deffender, fields, canvas):
        if(attacker.get_name() == deffender.get_name()):
            canvas = self.multiply(fields, canvas)
            return canvas

        if(attacker.get_strength()>=deffender.get_strength()):
            canvas = deffender.kill(fields, canvas)
            print(attacker.get_name(), end = ' ')
            print('killed', end = ' ')
            print(deffender.get_name())
            return canvas
        else:
            canvas = attacker.kill(fields, canvas)
            print(deffender.get_name(), end = ' ')
            print('killed', end = ' ' )
            print(attacker.get_name())
            return canvas

    def get_name(self):
        return self.name

    def get_location(self):
        return self.location

    def set_location(self, new_coords):
        self.location.x = new_coords.x
        self.location.y = new_coords.y

    def draw_organism(self, fields, canvas):
        for i in fields:
            if self.location.x == i.coords.x and self.location.y == i.coords.y:
                i.change_field(canvas, self.color)
                return canvas

    def draw_empty(self, fields, canvas):
        for i in fields:
            if self.location.x == i.coords.x and self.location.y == i.coords.y:
                i.change_field(canvas, 'Silver')
                return canvas