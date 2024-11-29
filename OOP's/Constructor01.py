class Student:
    def __init__(self,name,age):  #constructor
        self.name=name
        self.age=age

obj=Student("Shikher","20")
print(obj.name)
print(obj.age)
print(obj)