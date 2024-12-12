class Parent:
    def parent(self):
        print(Parent ,"in the Parent Class")

class Child(Parent):
    def child(self):
        print(Child)
        super().parent()
    def parent(self):
        print(Parent ,"in Child Class")
        super().parent()

    
obj= Child()
obj.parent()
obj.child()