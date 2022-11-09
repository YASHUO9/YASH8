a = [1,7,6,8,7,6,8,7]
 
 
def main(a,si,num):
    l = len(a)
    if l ==0:
        return print("no number")
    if a[si]==num:
        print(f"INDEX  NUMBER  :{si}")
        
    if si == l or si +1 >=l:
        return print("no more numbers")
    main(a,si+1,num)
ask_number = int(input("enter the number which you want to search in the array \n"))
main(a,0,ask_number)