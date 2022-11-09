array_1=[1,2,3,4,5,6,7,8]
#i have delete one and add one method used
def array_rotate1(n,i):
    if i<n:
        ok = array_1.pop(0)
        array_1.append(ok)
        i+=1
        array_rotate1(n,i)
    
            
        
array_rotate1(2,0)
print(array_1)
