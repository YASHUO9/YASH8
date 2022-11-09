class Node:
    """In this we have created the node"""
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
def printLL(head):
    """In this function we have print the link list"""
    i=0
    while head is not None:
        print(str(head.data)+ "->", end = "")
        head = head.next
        i+=1
    print("None")
    
    return

def Odd_Even(head):#In this i have divided the LL into 2 parts even and odd 
    ask = head
    odd = None
    even = None
    tail1 = None
    tail2 = None
    j = 0
    i = 0
    
    while head is not None:
        if ask is None:
            break
        if ask.data%2==0:
            if i ==0:
                even = ask
                tail1 = ask
                i+=1
            else:
                tail1.next = ask
                tail1 = ask
            ask = ask.next
            
        else:
            if j==0:
                odd = ask
                tail2 = ask
                j+=1
            else:
                tail2.next = ask
                tail2 = ask
            ask = ask.next
    tail2.next = even
    return odd
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
main = Odd_Even(head1)
printLL(main)

