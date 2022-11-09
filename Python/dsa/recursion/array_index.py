a = [1,2,3,4,5]

def main(a,si,number,lo):
    lo += si
    l = len(a)
    if l==0 or l+1 ==si:
        return False
    if number ==a[si]:
        return True
    check = main(a,si+1,number)
    
    return check
    
    
    
print(main(a,0,5))