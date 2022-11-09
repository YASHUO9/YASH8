try:
    num  = int(input("enter the number:"))
    num1 = int(input("Enter the number:"))
    if num1 ==0:
        raise ZeroDivisionError
    c = num +num1
    print(c)

except ZeroDivisionError:
    print("the denominator is zero here")
    
except ValueError:
    print("the value is not the number:")
except:
    print("the error is not defined here :")
    
    