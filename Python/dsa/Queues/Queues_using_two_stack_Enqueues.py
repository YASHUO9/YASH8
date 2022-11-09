class Queues:
    def __init__(self):
        self.data= []
        self.count = 0
        self.__front = 0
        self.q = Stack()
        self.q1 = Stack()
        self.new = 1
    def enqueues(self,item):#In this the complexity is of the order of O(n)
        if self.count >=1:
            for i in range(0,self.count):
                a = self.q.pop()
                self.q1.push(a)
            self.q.push(item)
            for i in range(0,self.count):
                b = self.q1.pop()
                self.q.push(b)
            self.count = self.count +1
            return
        self.q.push(item)
        self.count = self.count +1
    #In this the Dequeues is of the order of O(n)    
    def dequeues(self):
        #O(1)
         if self.count==0:
            print("Hey! Queues is Empty!!")
            return
         element = self.q.pop()
         self.__front+=1
         self.count = self.count -1
         return element
    def size(self):
        return self.count
    def isEmpty(self):
        return self.size() == 0
    def front(self):
        if self.count ==0:
            print("Hey! Queues is Empty!!")
            return
        return print(self.q.top())
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
        return self.__data[len(self.__data)-1]
    def size(self):
        return len(self.__data)
    def isEmpty(self):
        return self.size() ==0
q = Queues()
q.enqueues(1)
q.enqueues(2)
for r in range(0,2):
    print(q.dequeues())
