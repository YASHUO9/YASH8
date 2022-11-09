a = [1,2,3,4,5,6,7,8,9,10]
def better_sorted_array(a,si):
    l= len(a)
    if l-1 == si or l == si:
        return True
    if a[si]>a[si+1]:
         return False
    is_smallerlist_sorted = better_sorted_array(a,si+1)   
    return is_smallerlist_sorted
    
print(better_sorted_array(a,0))
