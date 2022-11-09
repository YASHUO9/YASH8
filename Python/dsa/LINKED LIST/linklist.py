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
          
class Node:
    """In this we have created the node"""
    def __init__(self,data):
        self.data = data
        self.next = None
def reverse(head,main):
    if head.next is None:
        main = head
        """here we have used the main to get the location or address of the last number """
        return head,main
    smallhead,Main = reverse(head.next,main)
    smallhead.next = head
    head.next = None
    return head,Main

def reverse3(head):
    """_summary_
      In this third version i have used the tail method to solve this 
    Args:
        head (_type_): _description_

    Returns:
        _type_: _description_
    """
    if head is None or head.next is None:
        return head
    small_head = reverse3(head.next)
    tail =  head.next
    tail.next = head
    head.next = None
    return small_head
head = takeInput()
printLL(head)
# main = None 
# head,main = reverse(head,main)
main = reverse3(head)
printLL(main)
"""The time complexity is of order of big O of "n" ok """