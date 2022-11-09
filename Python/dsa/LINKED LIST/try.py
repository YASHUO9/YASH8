class Node():
    def __init__(self,data):
       self.data = data
       self.next = None
    
def Input():
    ask = [int(ele) for ele in input().split()]
    head = None 
    tail = None
    for curr in ask:
        if curr == -1:
            break
        newNode = Node(curr)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
    return head
def printLL(head):
    while head is not None:
        print(str(head.data)+"->", end ="")
        head = head.next
    print("None")
    return
    


head = Input()
printLL(head)