
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
a = Node(12)
b = Node(13)

a.next = b
print(a.data)#12
print(b.data)#13
print(a.next.data)#`13
print(a)#address of a
print(a.next)#address of b
print(b)#address of b