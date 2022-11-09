class Queues:
    def __init__(self):
        self.data= []
        self.count = 0
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
    
q = Queues()
q.enqueues(1)
q.enqueues(2)
q.enqueues(3)
q.enqueues(4)
q.enqueues(5)
q.enqueues(6)


