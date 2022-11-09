def insert(head,i,data):
    if i<0:
        return head
    if i==0:
        new_Node = Node(data)
        new_Node.next = head
        return new_Node
    if head is None:
        return None
    smallhead = insert(head.next,i-1,data)
    head.next = smallhead
    return head
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

        
def printLL(head):
    while head is not None:
        print(str(head.data)+ "->", end = "")
        head = head.next
    print("None")
    return            
        
        
        
        
        
        
def takeInput():
    print("Enter the input as 1 2 3 4 5 -1 then it will work")
    inputList = [int(ele) for ele in input().split()]
    head =  None
    for currData in inputList:
        if currData == -1:
            break
        newNode = Node(currData)
        if head is None:
            head =  newNode
        else:
            curr = head
            while curr.next is not None:
                curr = curr.next
            curr.next = newNode
                
    return head
head = takeInput()
printLL(head)
insert(head,2,7)
printLL(head)
