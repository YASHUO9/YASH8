class complex:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag
        
    def add(self,other):
        self.real += other.real
        self.imag += other.imag
        print(f"{self.real} + i{self.imag}")
        
        
        
c1 = complex(1,2)
c2 = complex(3,4)


c1.add(c2)        
        
        
        
        
        
        
        
        
        
        