def main(a,si):
    l = len(a)
    
    #splitting the string into the list
    List = list(a)
    if l == si or l <si:
        mystring = ''.join(map(str,List))
        return print(mystring)
    if List[si] == "p" and List[si+1] =="i":
        List[si] = "3.1"
        a = ''.join(List)
        List[si+1] ="4"
        a = ''.join(List)
    main(a,si+1)
    
    
    
    
    
main("appipibypi",0)