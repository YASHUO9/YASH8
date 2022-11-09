def insertAtI(head,i, data):
    if i <0 or i>length(head):
        return head
    count = 0
    prev = None
    curr= curr.next
    while count <i:
        prev = curr
        curr = curr.next
        count  = count+1
         
    
    newNode  = Node(data)
    if prev is not None:
        prev.next= newNode
    else:
        head = newNode
    newNode.next = curr
            
    
    return head
def printLL(head):
    while head is not None:
        print(str(head.data)+ "->", end = "")
        head = head.next
    print("None")
    return    
    
   
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
    
    
    
    