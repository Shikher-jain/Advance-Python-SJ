# Functions with in class are methods

class Student:
    def __init__(self,name,age):  #constructor
        self.name=name
        self.age=age
    def show(self):
        print(self.name,self.age)

obj=Student("Shikher","20")
print(obj.name)
print(obj.age)
print(obj.show())

obj.show()