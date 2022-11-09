a =[3, 4, 5, 1, 2, 8]


# in the case of code each code position or algorithm is specific and each algorithm has a specific place to run the code
def quick(a, si):
    l = len(a)
    if a[si] > a[si+1]:
        partition(a,si)
        return

    if l == 0 or l < si+1:
        return
    if a[si] < a[si+1]:
        a[si], a[si+1] = a[si+1], a[si]
    

    quick(a, si+1)

def partition(a,si):
    i =1
    game_is_on = True
    while game_is_on:
        l = len(a)
        if l-1>si+i or si-i<=0:
            game_is_on = False
        if a[si] < a[si+i]:
            a[si],a[si+i] = a[si],a[si+i]
            a[si+i],a[si-1] = a[si-1],a[si+i]
            i+=1
        
        if a[si] > a[si-i]:
            a[si],a[si-i] = a[si],a[si-i]
            a[si-i],a[si+1] = a[si+1],a[si-1]
            i+=1
            
            
        
quick(a, 0)
print(a)
