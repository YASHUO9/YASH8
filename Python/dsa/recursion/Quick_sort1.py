a = [22,98,11,23,67,88,45,2,87,66,55,898,6,77,8,33,44]

def Quick_sort (si,ei,a):
    l = len(a)
    if l <=si+1:
        print(si)
        return
    if a[si] >a[si+1]:
        a[si],a[si+1] = a[si+1],a[si]
    else:
        partition(si,ei,a)
        print(si+1)
        partition(0,si+1,a)
        partition(si+1,len(a)-1,a)
        
        
        if a[si+1]<a[si]:
            a[si+1],a[si] = a[si],a[si+1]
            
        return
    Quick_sort(si+1,ei,a)
    
def partition(si,ei,a):

    
    if si+1>ei:
        return
    if a[si] > a[si+1]:
        a[si],a[si+1] = a[si+1],a[si]
    partition(si+1,ei,a)
    partition(si+1,ei,a)
    
    
    
    
Quick_sort(0,len(a)-1,a)
print(a)    
    
#done 