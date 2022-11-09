ask  = float(input("Enter the number of terms in the geometric series: "))

def main(n,k):
    if k == n:
        return 0
    else:
        ok = float(1/2**(k))
        return ok +main(n,k+1)
    
print(main(ask,0))
    
    