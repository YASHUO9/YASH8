class Stack:
    #for us it is an array and for the user it is stack
    def __init__(self):
        self.__data = []
        self.count  = 1
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
    def redundant_bracket(self):
        ok = self.size()
        for i in range(0,ok-2):
            a = self.pop()
            if self.isEmpty():
                return print("False")
            b = self.top()
            if "[" ==  a:
                if "[" ==  b:
                    return print("True")
                if "]" == b:
                    return print("True")
                else:
                    self.count = self.count +1
                    
            elif a == "]":
                if b == "]":
                    return print("True")
                elif self.count!=0:
                    return print("False")
                else:
                    self.count = self.count + 1
            else:
                self.count = self.count + 1

s = Stack()
main1 = "[a+b]"
main = "[[a+b]]"
print(main)
for i in main:
    s.push(i)

s.redundant_bracket()
