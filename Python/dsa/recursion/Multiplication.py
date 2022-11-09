ask = int(input("Enter the 1st number ?\n "))
ask01 = int(input("Enter the 2nd number ?\n "))

def multiply(a,b,c):
    if a == c:
        return 0
    else:
        sum = b + multiply(a,b,c+1)
        return sum
ok = multiply(ask,ask01,0)
print(ok)