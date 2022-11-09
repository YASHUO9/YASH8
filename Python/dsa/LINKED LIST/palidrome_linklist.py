


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
        
def palidrome(head):
    "In this firstly i have created the list to appened the data of the linked list"
    access_list = []
    main = head
    while head is not None:
        access_list.append(head.data)
        head = head.next
    length = len(access_list)
    top =0
    ask = False
    "here i have divided it into the 2 case for odd and even"
    if length%2!=0:
        "Is for odd number "
        while True:
            if length-top==1:
                break
            if access_list[top] ==access_list[length-1]:
                ask = True
            if access_list[top] !=access_list[length-1]:
                ask = False
                break
            top+=1
            length-=1
            
    else:
        "its for even number "
        while True:
            if top >length:
                break
            if access_list[top] ==access_list[length-1]:
                ask = True
            if access_list[top] !=access_list[length-1]:
                ask = False
                break
            top+=1
            length-=1
    
    if ask is True:
        print("Yes it is palidrome")
    else:
        print("it is not the palidrome")
        
           
    
head = takeInput()
printLL(head)
palidrome(head)

