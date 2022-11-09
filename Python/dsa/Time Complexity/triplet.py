import numpy as np
array = [2 ,-5, 8, -6, 0, 5 ,10 ,11, -3]

res = []
u=0
op=()
array1=[]
for i in range(0,len(array)):
    for j in range(0,len(array)-1):
        for k in range(0,len(array)-2):
            io =[]
            if array[i]+array[j]+array[k]==10 and array[i]!=array[j] and array[j]!=array[k] and array[k]!=array[i]:
                
                io.append(array[i])
                io.append(array[j])
                io.append(array[k])
                res.append(list(io))
                u+=1

ok =[]
op = np.array(res)

ok.append(op[0,0])
ok.append(op[0,1])
ok.append(op[0,2])
pl = list(ok)
print(pl)
print(u)
print(op)







