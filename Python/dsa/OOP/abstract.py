from abc import ABC,abstractmethod

class Automobile(ABC):
    print("Automobile created")
    
    @abstractmethod
    def start(self):
        print("Automobile started")
        pass
    @abstractmethod
    def stop(self):
        pass
    @abstractmethod
    def drive(self):
        pass
    
class Car(Automobile):
    def __init__(self,name):
    
        print("car created")
    
    
    # when we remove this comment the proogram will run again
    # but for now the abstract can not acquire the above class
    #while using the super function we can use the abstract classes
    
    def stop(self):
        
        
        pass
    def drive(self):
        pass
    def start(self):
        super().start()
          
    
    
c = Car("Honda")