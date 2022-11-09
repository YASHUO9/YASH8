def appened(head,position):
    z = 1
    main = head
    while head is not None:
        if head.next == None:
            break
        z+=1
        head = head.next
    position = z-position
    k=1
    curr =None
    head = main
    while head is not None:
        if k+1 ==z:
            curr = head
            print(curr.data)
            while head is not None:
                if head.next==None:
                    Tail = head
                    print(head.data)
                    head.next= main
                    
                    break
                head = head.next
            break
        k+=1
        head = head.next
        print(head.data)
    count = 2
    head  = main
    print(head.data)
    while head is not None:
        if count == k:
            print(head.data)
            head.next = None
            break
        count+=1
        head=head.next
        print(head.data)
    return curr
    
    
    
    
    
    
          
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
POSITION = int(input("Enter the position "))
CO = appened(head,POSITION)
printLL(CO)





