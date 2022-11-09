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
def circularLL(head):
    #In ths circularLL we have only connected the tail with the head so that the tail call the head not  to the None.
    ask = head
    while ask is not None:
        if ask.next is None:
            break
        ask = ask.next
    ask.next = head
    return ask
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
main = circularLL(head1)
print(((main.next).next).data)
