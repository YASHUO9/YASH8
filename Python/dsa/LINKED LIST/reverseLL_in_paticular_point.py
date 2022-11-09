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
def reverse(head):
    if head is None:
        return None
    ask = head       #1
    if ask.next is None:
        return None
    ask1 = ask.next  #2
    if ask1.next is None:
        return None
    ask2 = ask1.next #3
    if ask2.next is None:
        return None
    ask3 = ask2.next #4
    if ask4.next is None:
        return None
    ask.next = ask3  #1-->4
    ask2.next = ask1 #3-->2
    ask1.next = ask  #2-->1
    reverse(ask3)
    return ask2
        
#Time complexity of the linked list is big o of n2

head = takeInput()
printLL(head)

main = reverse(head)
printLL(main)

