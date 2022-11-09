a = [1,3,4,5,6,7,8,9,10]
def binarySearch(si,ei,num,a):
    if si>ei:
        return -1
    mid = (si +ei)//2
    if a[mid] == num:
        return mid
    elif a[mid] >num:
        return binarySearch(si,mid -1,num,a)
        
    else:
        return binarySearch(mid+1,ei,num,a)
ask = int(input("Enter the number you want to search ?"))
print(binarySearch(0,8,ask,a))
        