class Node:
    """In this we have created the node"""
    def __init__(self,data):
        self.data = data
        self.next = None
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
def Doubly_LL(head):
    curr = None
    i=0
    while head is not None:
        if curr is None and i ==0:
            curr = head
            curr.prev = None
            i+=1
        
        else:
        
            new = curr.next
            new.prev=curr
            curr= curr.next
            if head.next is None:
                break
        print("all ok")
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
main = Doubly_LL(head1)
print(main.prev)
