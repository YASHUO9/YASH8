# easiest question that i ever has faced in my life so easy question is of quick sort



a =[68,20,30,4,50,7,8,9,10]
def quick_sort(a,si):
    #in this 1st half i have sorted the half list
    l = len(a)
    if l == si or l <= si +1:
    
        return 
    if a[si]<a[si+1]:
        a[si],a[si+1] = a[si+1],a[si]
        quick_sort(a,si+1)
    quick_sort(a,si+1)
    
 

quick_sort(a,0)

print(a)

