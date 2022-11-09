ask = input("Enter the character to check it is fibbanico series is or not ?")
new =[]
#now i am spliting the word
for i in ask:
    new.append(i)

#now i am making the function to check it is fibbanico series or not
def check(new,k):
    l = len(new)-1-k
    if l == k:
        return print("Yes")
    if new[k] == new[l]:
        check(new,k+1)
    else:
        print("it is not the fibbanico series")
        
check(new,0)
