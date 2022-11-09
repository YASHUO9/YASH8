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
    
q = Queues()
q.enqueues(1)
q.enqueues(2)
q.enqueues(3)
q.enqueues(4)
q.enqueues(5)
q.enqueues(6)
while(q.isEmpty() is False):
    print(q.front())
    q.dequeues()
q.dequeues()
