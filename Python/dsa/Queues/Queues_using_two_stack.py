class Queues:
    def __init__(self):
        self.data= []
        self.count = 0
        self.__front = 0
        self.q = Stack()
        self.q1 = Stack()
        self.new = 1
    def enqueues(self,item):#In this the complexity is of the order of O(1)
        self.q.push(item)
        self.count = self.count +1
    #In this the Dequeues is of the order of O(n)    
    def dequeues(self):
        if self.count==0:
            print("Hey! Queues is Empty!!")
            return
        while self.count!=self.new:
            a = self.q.pop()
            self.q1.push(a)
            self.new = self.new + 1
        b = self.q.pop()
        for i in range(0,self.new-1):
            bew1 = self.q1.pop()
            self.q.push(bew1)
        self.new = 1
        self.__front+=1
        self.count = self.count -1
        return b
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
q.enqueues(3)
q.enqueues(4)
print(q.dequeues())
q.front()
i = 0
while i!=3:
    print(q.dequeues())
    i+=1

