


class Stack:
    #for us it is an array and for the user it is stack
    def __init__(self):
        self.__data =[]
        self.j = 2
        self.i = 0
    def push(self,item):
        self.__data.append(item)
    def pop(self):
        if self.isEmpty():
            print("Hey! Stack is Empty!!")
            return
        return self.__data.pop()
    def top(self):
        if self.isEmpty():
            print("Hey! Stack is Empty!!")
            return
        return self.__data[len(self.__data)-1]
    def size(self):
        return len(self.__data)
    def isEmpty(self):
        return self.size() ==0
    def compare(self):
        print("1",end="")
        while self.i!=6:
            a =self.pop()
            b = self.top()
            if a>=b:
                print("1",end="")
            else:
                print(f"{self.j}",end="")
                self.j = self.j +2
            self.i = self.i +1
            
def minium_bracket(arr):
    s = Stack()
    i = 0
    count =0
    for i in range(0,len(arr)):
        if len(arr)%2 == 0:
            curr = arr[i]
            if curr == "[":
                s.push(curr)
                count +=1
            elif curr == "]":
                if count == 0:
                    s.push(curr)
                    count +=1
                    
                else:
                    s.pop()
                    count-=1
            else:
                print("It is another element ")
            i+=1    
        else:
            return(print("-1"))
            
    if s.size !=0 :
        top1 = s.pop()
        top2 = s.top()
        if top1 != top2:
           count-=1
    print(count)
bracket = [ ele for ele in input().split() ]
minium_bracket(bracket)
    

