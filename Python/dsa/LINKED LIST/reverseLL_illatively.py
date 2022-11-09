def iteratively(head):   
    curr = head
    previous = None
 
    while curr is not None:
        next = curr.next
    
        curr.next = previous
        previous = curr

        curr = next
    head = previous
        
        
    return head
class Node:
    # """In this we have created the node""""
    def __init__(self,data):
        self.data = data
        self.next = None
        
def printLL(head):
    # """"In this function we have print the link list""""
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
head = takeInput()
printLL(head)
head = iteratively(head)
printLL(head)
               
