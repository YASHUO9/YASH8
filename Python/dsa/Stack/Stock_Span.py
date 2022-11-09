
def Stock_span(arr):
    i = 0
    print("1",end="")
    for j in range(0,len(arr)-1):
        a = int(arr[i])
        b = int(arr[i+1])
        if a >b:
            print("1",end = "")
        
        elif a <b :
            print(i+2,end = "")
        else:
            print("1",end = "")

        i+=1
        
stock_day = [i for i in input().split()]
Stock_span(stock_day)
