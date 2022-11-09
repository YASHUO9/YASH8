from tkinter import W


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

def duplicate(head):
    main =head
    if head == None:
        return None
    head = head
    while head is not None:
        curr = head
        Next = (head.next)
        if Next == None:
            break
        after_next = (head.next).next
        if curr.data == Next.data:
            curr.next = after_next
        head = head.next
        
    head = main
    while head is not None:
        if head.next == None:
            break
        if head.data == (head.next).data:
            ok = duplicate(head)
        head = head.next
    
    
    
    
    return main        
        
            
        


head = takeInput()
printLL(head)
main = duplicate(head)
Main = duplicate(main)
printLL(Main)
