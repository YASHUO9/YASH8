a = ["a","b","c","b","e"]

def main(a,si,n):
    l = len(a)
    c = "x"
    num = 1
   
    if l==si or l <si:
        return print(a)

        
    if a[si] == n:
        temp = a[si]
        a[si] = c
        c= temp 
        
        num+=1
        main(a,si+1,n)
        
        return True
        
        
    
    main(a,si+1,n)
    
    
main(a,0,"b")