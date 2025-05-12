class Student:
    def __init__(self,name,age):  #constructor
        self.name=name
        self.age=age

obj=Student("Shikher","20")
print(obj.name)
print(obj.age)

#Update the Data
obj.name="sj"
obj.age=22

print(obj.name)
print(obj.age)

#Delete the Data
del obj.age

print(obj.name)
# print(obj.age)  #  AttributeError: 'Student' object has no attribute 'age'

#Delete class
del obj
# print(obj.name) #   NameError: name 'obj' is not defined5


