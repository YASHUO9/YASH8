try:
    num = int(input("enter the number:"))
    num1  =  int(input("Enter the number:"))
    
except ValueError:
    print("invalid :")
    
try:
    a = 100
    b = 0
    c = a/b
    print(c)
    
except ValueError:
    print("invalid :")