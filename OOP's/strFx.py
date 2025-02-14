class Student:
    def __init__(self,name,age):  #constructor
        self.name=name
        self.age=age

obj=Student("Shikher","20")
# print(obj.name)
# print(obj.age)
print(obj)
print(str(obj))

class Student1:
    def __init__(self,name,age):  #constructor
        self.name=name
        self.age=age
    def __str__(self):
        return f"Name: {self.name} \nAge:{self.age}"

obj=Student1("Shikher","20")
# print(obj.name)
# print(obj.age)
print(obj)