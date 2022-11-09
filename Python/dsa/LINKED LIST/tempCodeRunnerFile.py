class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
def printLL(head):
    i=0
    while head is not None:
        print(str(head.data)+ "->", end = "")
        head = head.next
        i+=1
    print("None")
    print(i)
    return            
        
def search(head,num):
    j=0
    while head is not None:
        if head.data == num:
            print(f"the index is {j}")
            break
        if head == None:
            print("it is not present")
        head = head.next         
        j+=1
        
        
        
def takeInput():
    print("Enter the input as 1 2 3 4 5 -1 then it will work")
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
num = int(input("Enter the number you want to search in the link list :"))
search(head,num)

# Time complexity O(n2)
# Now the new time complexity of the code is O(n)