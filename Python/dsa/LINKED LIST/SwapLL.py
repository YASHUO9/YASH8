#This is in
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
def swap(head,pos1,pos2):
    if pos2-pos1 == 2 and pos1>0:
        curr1 = None
        curr2 = None
        prev1 = None
        prev2 = None
        main = head
        head = head
        for i in range(0,pos1-1):
            head = head.next
        prev1 = head
        curr1 = prev1.next
        head = main
        head = head
        for i in range(0,pos2-1):
            head = head.next
        prev2 = head
        curr2 = prev2.next
        head = main
        prev1.next = curr2
        prev2.next = curr1
        me = curr2.next
        curr1.next = me
        curr2.next = prev2
        return head
    if pos1+1 == pos2:
        head = head
        main = head
        curr1 = None
        curr2 = None
        prev1 = None
        prev2 = None
        for i in range(0,pos1):
            head = head.next
        curr1  = head
        curr2 = head.next
        prev = curr2.next
        curr1.next = prev
        head = main
        
#Time complexity of the linked list is big o of n2

head = takeInput()
printLL(head)
pos1 =int(input("Enter the 1st num and starting index num is 0"))
pos2 = int(input("Enter the 2nd num and starting index num is 0"))
main = swap(head,pos1,pos2)
printLL(main)

