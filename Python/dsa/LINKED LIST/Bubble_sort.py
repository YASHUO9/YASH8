class Node:
    """In this we have created the node"""
    def __init__(self,data):
        self.data = data
        self.next = None
        
def printLL(head):
    """In this function we have print the link list"""
    i=0
    while head is not None:
        print(str(head.data)+ "->", end = "")
        head = head.next
        i+=1
    print("None")
    
    return      
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
def bubble(head):
    curr = head
    prev = None
    game = True
    i=-3
    while game:
        if curr.next is None:
            curr = head
            prev = None
        if curr.data <(curr.next).data:
            new = curr.next
            prev = curr
            curr = new
            i+=1
        else:
            new = curr.next #
            new_next = new.next #
            prev.next = new 
            new.next = curr
            curr.next = new_next
            prev = curr
            curr = new
            i+=1
        if i == 5:
            game = False
    return head
#Time complexity of the linked list is big o of n2

head = takeInput()
printLL(head)

main = bubble(head)
printLL(main)

