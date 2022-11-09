array = [2,3,10,-10,4,2,9]
l = len(array)
def sum(array,i):
    sub=0
    sum=0
    for k in range(i+1,l):
        sum+=array[k]
    
    for m in range(0,i):
       sub+=array[m]
    if sum == sub:
        print(f"Equilibrium point index is {i} and value is {array[i]}")

for i in range(1,l-2):
    sum(array,i)
     