import turtle


class Entity:
    '''name,  shape, color, penup, stamp'''
    def __init__(self, *args) -> None:
        self.name = args[0]
        self.name = turtle.Turtle()
        self.name.shape('square')
        self.name.color(args[2])
        self.penup = args[3]
        self.stamp = args[4]
        self.shapesize = args[5]


        if self.penup == True:
            self.name.penup()

        if self.stamp == True:
            self.name.stamp()

    def postition(self, *args):
        self.name.goto(args[0], args[1])

    def clearstamps(self):
        self.name.clearstamps()