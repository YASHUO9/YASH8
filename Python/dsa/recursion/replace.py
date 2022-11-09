a = [1,2,3,4,5,6,7,8,9]


def main(si,a,num):
    l = len(a)
    if l==0 or l<si:
        return print("No Match found ")
    if a[si]== num:
        c = 100
        a[si] = K
        K = c   
        main(si+1,a,num)
        
    