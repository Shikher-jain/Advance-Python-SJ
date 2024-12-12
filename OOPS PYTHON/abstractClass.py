from abc import ABC, abstractmethod
print(dir())
class Button(ABC):
    @abstractmethod
    def click(self):
        pass
    def display():
        print("This is Display")

class Myclass(Button):
    def click(self):
        print("MY-CLASS")

class Photo(Button):
    def click(self):
        print("PHOTO")

M1=Myclass()
M1.click()
M2=Photo()
M2.click()
