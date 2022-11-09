def sorted_array(a):
    n = len(a)
    if n ==0 or n==1:
        return True
    if a[0] > a[1]:
        return False
    
    #it remove the 1st number of the array
    
    smallList = a[1:]
    isSmallerlistSorted = sorted_array(smallList)
    if isSmallerlistSorted:
        return True
    else:
        return False
        
        
main =[4,5,6]
print(sorted_array(main))