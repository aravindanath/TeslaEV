

class ExampleGlobal():

    # Global variable
    global wheelNo
    wheelNo = 5

    def __init__(self, colour):
        self.colour = colour

    def wheel(self):
        # Local variable
        wheelNo = 2
        print(wheelNo)
        print(self.colour)


    def carWheels(self):
        print(wheelNo)
        self.colour = "Green"
        print(self.colour)


exa = ExampleGlobal("red")

exa.carWheels()
exa.wheel()
