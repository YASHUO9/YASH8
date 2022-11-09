
a= [1,2,3,4,5,4]

length = len(a)




def main(a,num,length):
    if a[length-1]==num:
        return (print(f"index number from last : {length-1}"))
    if length <0:
        return print("no match:")
    main(a,num,length-1)
    
    
main(a,1,length)


