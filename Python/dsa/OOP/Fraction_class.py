
#here we are using the fraction class
#this Fractional class is use for the multiplication ,division and addition of fractions
class FractionClass:
    def __init__(self,num,den):
        self.num = num
        self.den = den
        
s = FractionClass(1,2)
ok = s.__dict__
print(ok)

# in this we have used the used the number in side the function so that it affect the class but it actually affect the class:
 
class Fraction:
    def __init__(self,num=1,den=2):
        self.num = num
        self.den = den
        
s1 = Fraction(0,8)
ok = s1.__dict__
print(ok)


