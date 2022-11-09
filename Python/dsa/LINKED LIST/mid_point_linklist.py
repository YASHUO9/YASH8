def mid(head):
    main = head
    i =0
    head = head
    while head is not None:
   
        head = head.next 
        i+=1  
    head = main
    if i%2==0:
        ans1 = int((i-1)/2)
        ans2 = int((i+1)/2)
        head = head
        for k in range(0,ans1):
            head = head.next
        print(head.data)
        head = main    
        for k in range(0,ans2):
            head = head.next
        print(head.data)      
    else:
        ans = int(i/2)
        head = head
        
        for k in range(0,ans):
            head = head.next
        print(head.data)                        
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

#Time complexity of the linked list is big o of n2

head = takeInput()
printLL(head)
mid(head)

