a =[1,2,3,4,5,6,7]
def main(a,si):
    l= len(a)
    if l+1 == si or l == si:
        return False
    if a[si]==7:
        return True
    is_smallerlist_sorted = main(a,si+1)   
    return is_smallerlist_sorted


print(main(a,0))





















