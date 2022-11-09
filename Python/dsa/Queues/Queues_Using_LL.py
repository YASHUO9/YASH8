class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Queues:
    def __init__(self):
        
        self.count = 0
        self.tail = None
        self.head = None
        
    def enqueues(self,item):
        if self.head == None:
            n = Node(item)
            self.head = n
            self.tail = n
            self.count +=1
            return
        n = Node(item)
        self.tail.next = n
        self.tail = n
        self.count = self.count +1
    def dequeues(self):
        if self.count==0:
            print("Hey! Queues is Empty!!")
            return
        ok = self.head
        self.head = self.head.next
        self.count = self.count -1
        return  ok.data
    def size(self):
        return self.count
    def isEmpty(self):
        return self.size() == 0
    def front(self):
        if self.count ==0:
            print("Hey! Queues is Empty!!")
            return
        return self.head.data
    
q = Queues()
q.enqueues(1)
q.enqueues(2)
q.enqueues(3)
q.enqueues(4)
while q.isEmpty() is False:
    print(q.dequeues())
q.dequeues()