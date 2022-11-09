#this problem is not completed
class Stack:
    #for us it is an array and for the user it is stack
    def __init__(self):
        self.__data =[]
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
        return self.__data(len(self.__data)-1)
    def size(self):
        return len(self.__data)
    def isEmpty(self):
        return self.size() ==0

def reverse(s1,s2):
    if s1.size() == 1:
        return

    a = s1.pop()
    b = s2.push(a)
    reverse(s1,s2)
    save = s1.pop()
    reverse(s2,s1)
    s1.push(save)
        
s = Stack()
new = Stack() 
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(s.size())
while s.isEmpty() is False:
    print(s.pop())
    
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print("Break")
reverse(s,new)
while s.isEmpty() is False:
    print(s.pop())
    




