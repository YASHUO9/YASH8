def reverse(head):
   """"in this we have created the reverse linked list"""
   if head is None:
        return None
   if head.next is None:
       return head 
   
   smallhead = reverse(head.next)
   curr = smallhead
   while curr.next is not None:
       curr = curr.next
   curr.next = head
   head.next = None 
   return smallhead
          
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

#Time complexity of the linked list is big o of n2

head = takeInput()
printLL(head)
head = reverse(head)
printLL(head)


