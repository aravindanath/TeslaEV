

class Car():

    def wheel(self):
        print("4 wheels")

    def door(self):
        print("4 doors")

class Bike():

    def cc(self):
        print("250 cc")

    def wheel(self):
        print("2 wheels")

class Bmw(Car,Bike):


    def colour(self):
        print("BMW Red colour")
        Bike.wheel(self)




b =  Bmw()

b.colour()
b.door()
b.wheel()
b.cc()