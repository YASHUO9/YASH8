class Queues:
    def __init__(self):
        self.data= []
        self.count = 0
        self.num = 1
    def enqueues(self,item):
        self.data.append(item)
        self.count = self.count +1
    def dequeues(self):
        if self.isEmpty():
            print("Hey! Stack is Empty!!")
            return
        self.count = self.count -1
        front =0
        return self.data.pop(front)
    def size(self):
        return self.count
    def isEmpty(self):
        return self.size() == 0
    def front(self):
        if self.isEmpty():
            print("Hey! Stack is Empty!!")
            return
        return self.data[self.count-1]
    def reverse(self,position):
        s = Stack()
        for i in range(0,position):
            a = self.dequeues()
            s.push(a)
        array = []
        for i in range(0,self.size()):
            remove = self.dequeues()
            array.append(remove)
      
        for i in range(0,position):
            previous = s.pop()
            self.enqueues(previous)
        for i in array:
            self.enqueues(i)
        self.data = self.data[::-1]    
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
print("before reverse to k = 4")
q.enqueues(1)
q.enqueues(2)
q.enqueues(3)
q.enqueues(4)
q.enqueues(5)
for i in range(0,5):
    print(q.dequeues())
q.enqueues(1)
q.enqueues(2)
q.enqueues(3)
q.enqueues(4)
q.enqueues(5)
q.reverse(4)
print("after reverse to k = 4")
for i in range(0,5):
    print(q.dequeues())



