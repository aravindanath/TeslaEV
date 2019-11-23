class Students():


    # THis is specal method works like constructor in java
    def __init__(self,name,age,sub):
        print("I am constructor")
        self.name = name
        self.age = age
        self.sub = sub

    def method1(self):
        print("Method...")

    def studentsAdm(self):
        print("Student name is ",self.name)
        print("Student subject is ",self.sub)

    # Method overloading is not possible in python
    def studentDetails(self,city):
        print("Student name ", self.name)
        print("Student is from  ", city)

    def studentDetails(self,city,collage):
        print("Student name ", self.name)
        print("Student is from  ", city)
        print("Student is from  ", collage)


s = Students("Harish","27","Python")
s.method1()
s.studentsAdm()
s.studentDetails("Bangalore","JGI")