

import time
def merge(a):
    if len(a) == 0 or len(a) == 1:
        return
    mid = len(a)//2
    a1 = a[0:mid]
    a2 = a[mid:]
    
    merge(a1)
    merge(a2)
    
    merge_sort(a1,a2,a)
    
def merge_sort(a1,a2,a):
    i=0
    j=0
    k=0
    while i<len(a1) and j<len(a2):
        if a1[i]<a2[j]:
            a[k]=a1[i]
            i+=1
            k+=1
        else:
            a[k]=a2[j]
            j+=1
            k+=1
    while i<len(a1):
        a[k]=a1[i]
        i+=1
        k+=1
    while j<len(a2):
        a[k]=a2[j]
        j+=1
        k+=1
def selection(a):
    for i in range(len(a)):
        min_idx = i
        for j in range(i+1,len(a)):
            if a[min_idx] > a[j]:
                min_idx = j
        a[i],a[min_idx] = a[min_idx],a[i]
        
        
        
def create_rev_array(n):
    a = []
    for i in range(n,0,-1):
        a.append(i)
    return a

a = create_rev_array(10)
start = time.time()
print(start)
op = selection(a)
end = time.time()

print(a)
print(len(a),end-start)

# start = time.time()
# op = selection(a)
# end = time.time()
# print(a)
# print(len(a),end-start)




