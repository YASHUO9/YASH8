a= [1,2,3,4,5]
def main(a,b,si):
    l = len(a)
    if b ==a[0]:
        return True
    if l ==si :
        return False
    do = main(a[:1],b,si+1)
    
    
print(main(a,5,0))