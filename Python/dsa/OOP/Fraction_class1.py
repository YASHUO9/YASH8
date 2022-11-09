class Fraction:
    def __init__(self,den,num):
        self.num = num
        self.den = den
        
    def add(self):
        ok = s1.num*s2.den + s2.num*s1.den
        ji = s2.den*s1.den   
        si = ok//ji
        print(si)
        
s1 = Fraction(1,0)

s2 = Fraction(2,0)


s1.add()