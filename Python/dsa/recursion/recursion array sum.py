def array_sum(a,n):
    
    if len(a)==1:
        return a[0]
    else:
       return a[0]+array_sum(a[1:],n)
    
    
    
a =[1,2,3,4,5]
n = len(a)
p = array_sum(a,n)
print(p)