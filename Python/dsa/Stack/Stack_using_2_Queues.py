class Queues:
    def __init__(self):
        self.data= []
        self.count = 0
        self.__front = 0
    def enqueues(self,item):
        self.data.append(item)
        self.count = self.count +1
    def dequeues(self):
        if self.count==0:
            print("Hey! Queues is Empty!!")
            return
        element = self.data[self.__front]
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
        return self.data[self.__front]
    
class Stack:
    #for us it is an array and for the user it is stack
    def __init__(self):
        self.q = Queues()
        self.q1 = Queues()
        self.count = 0
    def push(self,item):
        self.q.enqueues(item)
        self.count = self.count+1
        
    def pop(self):
        if self.isEmpty():
            print("Hey! Stack is Empty!!")
            return
        i=1
        if self.count>=i:
            for r in range(0,self.count-1):
                a = self.q.dequeues()
                self.q1.enqueues(a)
            b = self.q.dequeues()
            for r in range(0,self.count-1):
                ok = self.q1.dequeues()
                self.q.enqueues(ok)
            self.count = self.count-1
            return b
        return self.q.dequeues()
    def top(self):
        if self.isEmpty():
            print("Hey! Stack is Empty!!")
            return
        return self.q.front()
    def size(self):
        return self.q.size()
    def isEmpty(self):
        return self.q.size ==0


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
for i in range(0,4):
    print(s.pop())
    
