a = [1,2,4,5,6,7,8,9,10]

def index(a,si,num):
    k=0
    k+=si
    l = len(a)
    if a[si]==num:
        
        return print(f"INDEX NUMBER IS {si}")
    if si == l or si +1 >=l:
        
        return print(-1)
    
    return index(a,si+1,num)
jack = int(input("Enter the number you want to search in the array:\n"))
index(a,0,jack)