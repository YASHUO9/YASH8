import sys
sys.setrecursionlimit(5000)
print(sys.getrecursionlimit())
number = int(input("Enter the number:"))
power_ =int(input ("enter the  power:"))


def power(actual_power,actual_number):
    if actual_power ==0:
        return 1 
    else :
        return actual_number*power(actual_power-1,actual_number)


print(power(power_,number))