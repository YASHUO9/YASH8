a = [1,2,3,4,5]


def to_sorte_list(a,si):
    l = len(a)
    if l == si+1 or l <si:
        return a
    if a[si] < a[si+1]:
        a[si],a[si+1] = a[si+1],a[si]
    to_sorte_list(a,si+1)
    
    
ok  = to_sorte_list(a,0)
print(ok)        
    