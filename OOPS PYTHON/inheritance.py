# class Employee:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id

#     def show(self):
#         print(f"Name of Employee  {self.id} is {self.name}")

# # Programmer USE Employee FUNCTION                              #Single inheritance
# class Programmer(Employee):                                     #Multiple inheritance
#     def showLang(self):                                         #Multilevel inheritance
#         print("PYTHON")                                         #Hierarchical inheritance
#         print("OOPS")                                           #Hybrid inheritance

# class Freshers(Programmer):
#     def ShowFresher(self):
#         print("THIS CLASS FOR FRESHERS ONLY !!!")

# e1=Employee("Shikher Jain",75)
# e1.show()
# e2=Employee("Sonu Jain",9)
# e2.show()
# e3=Employee("Shikher ",89)
# e3.show()
# e4=Programmer("SJ",2004)
# e4.showLang()
# e5=Freshers("FRESHERS",1234)
# e5.showLang()
# e5.show()
# e5.ShowFresher()

#++++++++++SINGLE++++++++++++

# class Animal:
#     def __init__(self,name,species):
#         self.name=name
#         self.species=species
#     def sound(self):
#         print("Sound made By Animal")

# class Dog(Animal):
#     def __init__(self,name,breed):
#         Animal.__init__(self,name,species="Dog")
#         self.breed=breed
#     def sound(self):
#         print("Bark!!")

# d=Dog("Dog","Doggerman")
# d.sound()

# a=Animal("Dog","Doggy")
# a.sound()

# ++++++++++++MULTIPLE++++++++++++

# class Emp():
#     def __init__(self,name):
#         self.name=name

# class Coder():
#     def __init__(self,lang):
#         self.lang=lang
#         print(f"Name is {self.name}")
# class EmpCoder(Emp,Coder):
#     def __init__(self,lang,name):
#         self.lang=lang
#         self.name=name
#     def show(self):
#         print(f"Language is {self.lang}")

# obj=EmpCoder("Python","XYZ")
# print(obj.lang)    
# print(obj.name)    
# obj.show() #jo pahle class me likha hia wahi ayega e.g. : line 64 Emp,Coder so Emp's shw function run
# print(EmpCoder.mro())

# +++++++++++++++++++MULTILEVEL++++++++++++++++++

# class BaseClass:
# class DerivedClass1(BaseClass):
# class DerivedClass2(DerivedClass1):

# class Animal:
#     def __init__(self,name,species):
#         self.name=name
#         self.species=species
#     def details(self):
#         print(f"Name:{self.name}")
#         print(f"Species:{self.species}")

# class Dog(Animal):
#     def __init__(self,name,breed):
#         Animal.__init__(self,name,species="Dog")
#         self.breed=breed
#     def details(self):
#         Animal.details(self)
#         print(f"Breed:{self.breed}")


# class Dog2(Dog):
#     def __init__(self,name,color):
#         Dog.__init__(self,name,breed="Bull Dog")
#         self.color=color
#     def details(self):
#         Dog.details(self)
#         print(f"Color:{self.color}")


# # d=Dog("Dog1","Dog")
# # d.details()

# # a=Animal("Dog2","German Sheperd")
# # a.details()

# d2=Dog2("Dog3","black")
# d2.details()
# print(Dog2.mro())

# +++++++++++++++Hybrid++++++++++++++++
# Mixture Of All Above Types Of Heritance
class BaseClass:
    pass
class Derived1(BaseClass):
    pass
class Derived2(BaseClass):
    pass
class Derived3(Derived1,Derived2):
    pass

# +++++++++++++++Hieararchical++++++++++++++++
class BaseClass:
    pass
class Derived1(BaseClass):
    pass
class Derived2(BaseClass):
    pass
class Derived3(Derived1):
    pass
class Derived3(Derived2):
    pass
