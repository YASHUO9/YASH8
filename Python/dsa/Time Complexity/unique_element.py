#this program is used for the find the time complexity of the function have the repeated value as we have to find the unique value
array = [1,2,3,2,6,1,6,8]

#this 1st loop is running for the one value 
for i in range(0,len(array)):
    k=0
    
    #This 2nd loop is running for comparing the 1st value of the loop 
    for j in range(0,len(array)):
       if array[i] ==array[j]:
        k+=1
    #the single value to be print 
    if k<2:
        print(f"the number is unique {array[i]}")
      

#time complexity is O(n2)