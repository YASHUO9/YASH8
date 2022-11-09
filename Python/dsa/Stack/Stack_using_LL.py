

class Node:
    """In this we have created the node"""
    def __init__(self,data):
        self.data = data
        self.next = None
        

class Stack:
    #for us it is an array and for the user it is stack
    def __init__(self):
       self.__head = None
       self.__count = 0
        
    def push(self,element):
        
        new_Node  = Node(element)
        new_Node.next = self.__head
        self.__head = new_Node
        self.__count = self.__count +1 
        
    def pop(self):
        if self.isEmpty() is True:
            print("Hey! Stack is Empty!!")
            return
        data = self.__head.data
        self.__head = self.__head.next
        self.__count = self.__count -1
        return data
    def top(self):
        if self.isEmpty() is True:
            print("Hey! Stack is Empty!!")
            return
        data = self.__head.data
        return data
    def size(self):
        return self.__count
    def isEmpty(self):
        return self.size()==0


class Node:
    """In this we have created the node"""
    def __init__(self,data): 
        self.data = data
        self.next = None
        




s = Stack()
s.push(12)
s.push(13)
s.push(15)

while s.isEmpty() is False:
    print(s.pop())
s.pop()
s.top()





















