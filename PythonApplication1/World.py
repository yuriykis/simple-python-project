from tkinter import*
from Human import*
from Field import*
from Organism import*
from Wolf import*
from Fox import*
from Sheep import*
from Antelope import*
from Turtle import*
from Cybersheep import*
from Grass import*
from Hogweed import*
from Beladonna import*
from Guarana import*
from SowThistle import*


class World(object):

    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def initialise(self):
        self.win = Tk()
        self.win.title("World")
        self.canvas = Canvas(self.win, width = 800, height = 800, bg = "silver")
        self.canvas.pack()
        self.fields = []
        self.organisms = []


    def add_organism(self, coords, name):
        if(name == 'Human'):
            z = Human(self, 'Human', 1, coords, 'Blue')
        elif(name == 'Wolf'):
            z = Wolf(self, 'Wolf', 9, coords, 'Black')
        elif(name == "Fox"):
            z = Fox(self, 'Fox', 3, coords, 'Orange')
        elif(name == "Sheep"):
            z = Sheep(self, 'Sheep', 4, coords, 'White')
        elif(name == "Antelope"):
            z = Antelope(self, 'Antelope', 4, coords, 'Red')
        elif(name == "Turtle"):
            z = Turtle(self, 'Turtle', 2, coords, 'Green')
        elif(name == "Cybersheep"):
            z = Cybersheep(self, 'Cybersheep', 3, coords, 'White')
        elif(name == "Grass"):
            z = Grass(self, 'Grass', 0, coords, 'Palegreen')
        elif(name == "SowThistle"):
            z = SowThistle(self, 'SowThistle', 0, coords, 'Yellow')
        elif(name == "Guarana"):
            z = Guarana(self, 'Guarana', 0, coords, 'Violet')
        elif(name == "Beladonna"):
            z = Beladonna(self, 'Beladonna', 100, coords, 'Saddlebrown')
        elif(name == "Hogweed"):
            z = Hogweed(self, 'Hogweed', 100, coords, 'Teal')
        self.organisms.append(z)

    def delete_organism(self, coords):
        for i in self.organisms:
            if i.location.x == coords.x and i.location.y == coords.y:
                self.organisms.remove(i)
                break

    def is_empty(self, coords):
        for i in self.organisms:
            if(i.location.x == coords.x and i.location.y == coords.y):
                return False
        return True

    def free_random(self, loc):
        counter = 0
        coords = Coords(randrange(1,20,2), randrange(1,20,2))
        while counter<20:
            if self.is_empty(coords):
                return coords
            else:
                coords = Coords(randrange(1,20,2), randrange(1,20,2))
                counter += 1
        else:
            coords = loc
            return coords

    def check_field(self, coords):
        for i in self.organisms:
            if i.location.x == coords.x and i.location.y == coords.y:
                return i;
            else:
                return None

    def update_canvas(self, canvas):
        for i in self.organisms:
            canvas = i.draw_organism(self.fields, self.canvas)
        return canvas

    def start(self):
      self.initialise()
      for i in range(20):
          for j in range(20):
              coords = Coords(i,j)
              f = Field(coords)
              self.fields.append(f)
              self.canvas = f.draw_field(self.canvas)
      human_location = Coords(8,4)
      self.add_organism(human_location, 'Human')
      #self.add_organism(Coords(2,2), 'Human')
      self.add_organism(Coords(5,5), 'Wolf')
      self.add_organism(Coords(10,5), 'Fox')
      self.add_organism(Coords(13,5), 'Fox')
      self.add_organism(Coords(3,5), 'Turtle')
      self.add_organism(Coords(11,13), 'Antelope')
      self.add_organism(Coords(12,13), 'Antelope')
      self.add_organism(Coords(14,10), 'Grass')
      self.add_organism(Coords(16,10), 'SowThistle')
      self.canvas = self.update_canvas(self.canvas)
      self.turn()

    def right(self, event):
        for i in self.organisms:
            self.canvas = i.action(self.fields, self.canvas, 'Right')

    def left(self, event):
        for i in self.organisms:
            self.canvas = i.action(self.fields, self.canvas, 'Left')

    def up(self, event):
        for i in self.organisms:
            self.canvas = i.action(self.fields, self.canvas, 'Up')

    def down(self, event):
        for i in self.organisms:
            self.canvas = i.action(self.fields, self.canvas, 'Down')

    def turn(self):
        self.win.bind('<Right>', self.right)
        self.win.bind('<Left>', self.left)
        self.win.bind('<Up>', self.up)
        self.win.bind('<Down>', self.down)
        self.win.mainloop()
    