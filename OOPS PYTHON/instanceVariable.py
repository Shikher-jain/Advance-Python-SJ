class Employee:
    companyName="JST"   #CLASS VARIABLE
    noOfEmployee=0
    def __init__(self,name):
        self.name=name  #INSTANCE VARIABLES
        self.fees=99    #INSTANCE VARIABLES
        Employee.noOfEmployee+=1
    def details(self):
    # def details():
        print(f"{self.noOfEmployee} Empolyee Name is {self.name} and fees is {self.fees} in {self.companyName}")

emp1=Employee("Shikher")
emp1.fees=100
emp1.companyName="JST 01"
emp1.details()
emp2=Employee("Shikher Jain")
emp2.details()
# Employee.details(emp1) #with or without self
print("TOTAL EMPOLYEE ARE :\n",Employee.noOfEmployee)