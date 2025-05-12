# class Car:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.__model = model

#     @property
#     def model(self): #overriding
#         return self.__model    
    
#     @staticmethod
#     def description():
#         return "TRANSPORTATION"
    
#     def full(self):    
#         return f"Brand: {self.brand} \nMode : {self.model}"
    
#     def __str__(self):
#         return f"Brand: {self.brand} \nMode : {self.model}"    
    
#     def fuel(self): #overriding
#         return "Petrol Or diesel"

# class EV(Car): #inheritance
#     def __init__(self,brand,model,size):
#         super().__init__(brand,model)
#         self.size = size
    
#     def fuel(self): #overriding
#         return "Electric "

# obj = Car("BMW", "X5")
# print(obj.model)
# print(obj.model)
# print(obj.brand)

# print(obj.description())
# print(Car.description())

# print(obj.model)
# print(obj)
# # print(obj.full())
# ev = EV("Tesla", "Model S", "4x4")
# print(ev.full())
# print(ev.fuel()) #overriding
# print(obj.fuel()) #overriding

# #encapsulation

# class Student:    
#     def __init__(self,name,age):
#         self.__name=name
#         self.__age=age

#     def get_name(self):
#         return self.__name
    
#     def get_age(self):
#         return self.__age
    
#     def set_name(self,name):
#         self.__name=name

#     def set_age(self,age):
#         self.__age=age    
    
#     def __str__(self):
#         return f"Name: {self.__name} \nAge:{self.__age}"

# obj = Student("Shikher", 20)
# print(obj)
# print(obj.get_name())
# print(obj.get_age())
# obj.set_name("Shikher JAIN")
# obj.set_age("21 !!!")
# print(obj.__age) #error
# print(obj.age) #error
# print(obj)

# print(isinstance(ev, Car))
# print(isinstance(Car,Student))
# print(isinstance(ev,Student))
# print(isinstance(obj,Student))

class A:
    def __init__(self):
        print("A")

    def showA(self):
        print("A Show")

class B:
    def __init__(self):
        print("B")

    def showB(self):
        print("B Show")

class C(A,B):
    def __init__(self):
        # super().__init__()
        print("C")

    def showC(self):
        print("C Display")

obj = C()

obj.showA()
obj.showB()
obj.showC()