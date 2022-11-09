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
def mergeLL(head1,head2):
    "This function is used to merge two different linklist :"
    curr1 = head1
    curr2 = head2
    """After is used as a helper between the head1 and head2"""
    after = None
    while curr1 is not None and curr2 is not None:
        if curr1.data > curr2.data:
            after = curr2.next
            curr2.next = curr1
            curr2 = after
        else:
            after = curr1.next
            curr1.next = curr2
            curr1 = after
    return head1
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
head2 = takeInput()
printLL(head1)
printLL(head2)
main = mergeLL(head1,head2)
printLL(main)