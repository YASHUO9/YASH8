ask = int(input("enter the number to find the sum of these serie ?\n "))

def sum(n,r):
    if r==n:
        return
    else:
        
        sum = r+sum(n,r+1)
        
sum(ask,0)    

