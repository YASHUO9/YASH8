class Node:
    """In this we have created the node"""
    def __init__(self,data):
        self.data = data
        self.next = None
        """In this prev is stand for the previous element data or address location .        """
        self.prev = None
def printLL(head):
    """In this function we have print the link list"""
    i=0
    while head is not None:
        print(str(head.data)+ "->", end = "")
        head = head.next
        i+=1
    print("None")
    
    return      
def Doubly_Linklist(head):
    " In this we have taken the doubly linked list in which each data is linked with each other :"
    new = None
    self = head
    i=0
    while head is not None:
        if new is None and i ==0:
            new = head
            new.prev = None
            new = new.next
            i+=1
        else:
            if new is None:
                break
            new.prev = self
            self = new
            new = new.next
            
    return head      
def takeInput():
    inputList = [int(ele) for ele in input().split()]
    head =  None
    tail = None
    for currData in inputList:
        if currData == -1:
            break
        newNode = Node(currData)
        if head is None:
            head =  newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
                
    return head

#Time complexity of the linked list is big o of n2

head1 = takeInput()
printLL(head1)
net  = Doubly_Linklist(head1)
#The output must be one you can check by your self
print(((net.next).prev).data)
