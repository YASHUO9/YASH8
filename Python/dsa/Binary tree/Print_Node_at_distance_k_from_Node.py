def treeinput():
    element = int(input())
    if element  == -1:
        return None
    ele = BinaryTreeNode(element)
    leftTree = treeinput()
    rightTree = treeinput()
    ele.left = leftTree
    ele.right = rightTree
    return ele
    
def print_Kth(root,position,i):
    if root == None:
        return
    if position == i:
        print(root.data)
        return
    left = print_Kth(root.left,position,i+1)
    right = print_Kth(root.right,position,i+1)
    #This substraction due to the returning in the previous function
    i=-1
    
class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def printTreeDetailed(root):
    if root == None:
        return
    print(root.data,end = ":")
    if root.left != None:
         print("L",root.left.data, end = " ,")
    if root.right!= None:
        print("R",root.right.data,end = "" ) 
    print()
    printTreeDetailed(root.left)
    printTreeDetailed(root.right)


root  = treeinput()
position = int(input("Enter the value of kth position :\n"))
i = 1
print_Kth(root,position,i)


