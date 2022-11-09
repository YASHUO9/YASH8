try:
    num = int(input("enter the number:"))
    num1 = int(input("Enter the number:"))
    if num1 == 0:
        raise ZeroDivisionError
    a = num/num1
    print(a)
    
except ZeroDivisionError:
    print("ZeroDivisionError")