ask = input("Enter the charater ?\n")
ask1 = []

for i in ask:
    ask1.append(i)
def check(a,si,ei):
    
    if ei<=si:
        return a
        
    if a[si] == a[si+1]:
       a.insert(si+1,"*")  
    check(a,si+1,ei)
    
    
check(ask1,0,len(ask1)-1)
ask = "".join(ask1)




