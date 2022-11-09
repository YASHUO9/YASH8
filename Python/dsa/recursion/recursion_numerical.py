#In this question we have to find the sum of the number 1 to n.
number = int(input("Enter the number:"))


def number1(num):
    if num ==0:
        return 
    else:
        print(num)       
        number1(num-1)
        return 
def number12(num):
        
        if num == 0 :
           return 0
        number12(num-1)
        print(num)
        return
        
    
number1(number)
number12(number)