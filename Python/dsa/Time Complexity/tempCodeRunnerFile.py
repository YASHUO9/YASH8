import numpy as np

array1 = [[2,8,0],[2 , 0 , 8],[-5,5, 10],[-5, 10 , 5],[ 8 , 2 , 0],[ 8 , 0 , 2],[-6 ,11 , 5],[ 0,  2 , 8],[ 0 , 8  ,2],[ 5 ,-5, 10],[ 5 ,10, -5],[ 5 ,11, -6],[10 ,-5 , 5],[10 , 5, -5],[11 ,-6,  5],[11 , 5, -6],[-3 ,8 , 5],[-3 , 5 , 8],[-3 ,11,  2]]
op = np.array(array1)
for i in range(0,3):
    m=0
    ok=[]
    for j in range (0,3):
        ok.append(op[i,j])
        m+=1
        
        if m==3:
            ok = len(array1)
            
            for k in range(0,ok):
                print(f"{array1[k]},{ok[0]},{ok[1]},{ok[2]} ")
                # if f"[{ok[0]},{ok[2]},{ok[1]}]"==f"{array1[k]}":
                #     print("y")
                #     del array1[k]
                #     ok = len(array1)
            #     if [ok[1],ok[0],ok[2]]==array1[k]:
            #         print(array1[k])
            #         del array1[k]
            #         ok = len(array1)
            #     if [ok[1],ok[2],ok[0]]==array1[k]:
            #         print(array1[k])
            #         del array1[k]
            #         ok = len(array1)
            #     if [ok[2],ok[0],ok[1]]==array1[k]:
            #         print(array1[k])
            #         del array1[k]
            #         ok = len(array1)
            #     if [ok[2],ok[1],ok[0]]==array1[k]:
            #         print(array1[k])
            #         del array1[k]
            #         ok = len(array1)

print(array1)
