ask = [ i for i in input()]
print(ask)
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','+','-','*']



#This program is used to find the balanced bracket Like (({{}})) or (a+b)
class Stack:
    #for us it is an array and for the user it is stack
    def __init__(self):
        self.__data =[]
        self.count = 0
        
    def push(self,item):
        if "[" ==item or "(" ==item or "{" == item:
            self.__data.append(item)
            self.count = self.count +1
        if  "]" ==item or ")" ==item or "}" == item:
            a = item
            b = self.__data.pop()
            if a=="]" and b=="[" or a=="}" and b=="{" or a==")" and b=="(":
                self.count = self.count - 1
            else:
                return print("False")
        if self.count == 0:
            return print("True")
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
    
s = Stack()

for i in alphabet :
    for j in ask:
        if i ==j:
            ask.remove(i)
for i in ask:
    s.push(i)


