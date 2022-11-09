#it helps to see the actual list
list = [1, 2, 3, 4, 8,90,5, 6,7,9]


    

#this function is used to maintain the 2 list to form the new original list
def merge(a1,a2,a):
    
    i = 0
    j = 0
    k = 0
     # here we were checking the number is greater or not
    while i < len(a1) and j < len(a2):
        
        if a1[i] <a2[j]:
           a[k] = a1[i] 
           i += 1
           k+=1
        else:
            a[k] = a2[j]
            k+=1
            j+=1
            
    #if the list is left then here we can again copy paste the number to the new list
    while i < len(a1):
        a[k] = a1[i]
        k+=1
        i+=1
    while j <len(a2):
        a[k] =a2[j]
        j+=1  
        k+=1



#this is the main branch of the file here we take the main list and divide it not to sub part
def merge_sort(a):
    if len(a) == 0 or len(a) ==1:
        return 
    
    mid = len(a)//2
    a1 = a[0:mid]
    a2 = a[mid:]
    
    merge_sort(a1)
    merge_sort(a2)
    
    merge(a1,a2,a)  
    
            
(merge_sort(list))    
print(list)   

            

