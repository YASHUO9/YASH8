ask = int(input("enter the number to find the sum of these serie ?\n "))

def sum(si,ei):
    if si == ei:
        return si
    sum_ = si +sum(si+1,ei)
    return sum_ 
ok = sum(0,ask) 
print(ok)   

