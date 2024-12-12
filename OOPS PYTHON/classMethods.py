# class Student:
#     work="XYZ"
#     def show(self):
#         print(f"{self.name} is in Company {self.work}")

#     def changeWork(cls,newWork):
#        cls.work=newWork

# s1=Student()
# s1.name="Shikher"
# s1.show()
# s1.changeWork("ABCD")
# s1.show()
# print(s1.work)
# print(Student.work)
# print(s1 is Student)
# print(s1 == Student)


# class Student2:
#     work="XYZ"
#     def show(self):
#         print(f"{self.name} is in Company {self.work}")
#     @classmethod
#     def changeWork(cls,newWork):
#        cls.work=newWork

# s1=Student2()
# s1.name="Shikher"
# s1.show()
# s1.changeWork("ABCD")
# s1.show()
# print(s1.work)
# print(Student2.work)
# print(s1 is Student2)
# print(s1 == Student2)

# print(Student == Student2)
# print(Student is Student2)

# ALTERNATIVE CONSTRUCTOR

class Employee:
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary
    
        print(f"Employee Named {name}'s Salary is {salary}")
    
    @classmethod
    def fronstr(cls,string):
        return Employee(string.split("-")[0],string.split("-")[1])

e=Employee("Shikher",25000)
string = "Shikher jain-55000"
e1=Employee.fronstr(string)
