from abc import ABC, abstractmethod   
class father(ABC):
    def car(self):
        pass
class son(father):
    def car(self):
        print("you accessed your car")
class daughter(father):
    def car(self):
        print("you accessed the key")
x=son()
x.car()
y=daughter()
y.car()
