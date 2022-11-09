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

def deleteLL(head):
    #"In this we have make LL in which two element are present and other 3 has to be removed"
    present = 2
    main = head
    after = None
    while head.next is not None:
        c1=1
        while  head is not None:
            if c1 ==present:
                break
            if after  is None:
                after = main.next
                print(after.data)
            else:
                new = after
                print(new.data)
                after = new.next
            c1+=1
        new1 = after
        ok = None
        for i in range(0,4):
            if new1.next is None:
                break
            ok =new1
            new1 = ok.next
            print(new1.data)
        after.next = new1
        print(after.data)
        after = new1
        print(after.data)
        so = after.next
        if after.next is None or so.next is None:
            break
    return head
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
main = deleteLL(head1)
printLL(main)



