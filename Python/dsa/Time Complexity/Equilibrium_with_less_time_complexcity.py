def equili():

    array = [2,3,10,-10,4,2,9]
    total_sum = 0
    i=0
    while i <len(array):
        total_sum +=array[i]
        i+=1
    left_sum=0
    index = 0    
    while index<len(array):
        right_sum = total_sum  - array[index]-left_sum
        if right_sum == left_sum:
            print(index)
        left_sum += array[index]
        index+=1
    


print(equili())
