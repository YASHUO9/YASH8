      
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
        
def insert(head,data,position):
    # In this 1st we have consider the head to be changed
    if position == 0:
        new_node = Node(data)
        new_node.next = head
        head = new_node
        return head
    #In this 2nd we have consider the tail to be removed 
    z = 0
    ok = None
    main = head
    while head is not None:
        if head.next is None:
            break
        head = head.next
        z+=1
    #In this we have consider the middle case between the tail and head    
    head = main    
    previous = None    
    if z+1 == position:
        new_node = Node(data)
        equal = 0
        while equal is not z:
            head = head.next
            print(head.data)
            equal += 1
        head.next = new_node
        return main
    j=0
    newo =head
    curr = None
    previous = None
    new_node = None
    while head is not None:
        if position ==1:
            if j== position:
                new_node = Node(data)
                new = curr
                previous.next = new_node
                new_node.next = curr 
                return head
            else:
                previous = head
                curr= head.next      
                j+=1
        if j== position:
                new_node = Node(data)
                new = curr
                previous.next = new_node
                new_node.next = curr 
                return newo
        else:
            previous = head
            if j>=1:
                previous = head.next
            
            curr =head.next
            if j>=1:
                head = head.next
                curr = head.next
            
            j+=1
        
        
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
def search(head,num):
    a=0
    while head is not None:
        if head.next == None:
            print("data is not present in the linked list:")
            break
        if head.data == num:
            print(f"data is present in the linked list at the present at index {a} ")
            break
        a+=1
        head = head.next





















head = takeInput()
#printLL(head)
data = int(input("Enter the number you want to insert in the link list:"))
position = int(input("Enter the position you want to insert in the link list:"))
head = insert(head,data,position)
search = int(input("Enter the number you want to search in the link list:"))
search(head,search)
printLL(head)
# Time complexity O(n2)
# Now the new time complexity of the code is O(n)



