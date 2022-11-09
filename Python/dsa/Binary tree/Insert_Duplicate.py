#print kth element of the binary tree

def insert_Duplicate(root):
    if root ==  None:
        return None
    new = BinaryTreeNode(root.data)
    left = root.left
    right = root.right
    root.left = new
    new.left = left
    new.right = None
    new_left = insert_Duplicate(left)
    new_right = insert_Duplicate(right)
    
    
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
    
#copy
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
printTreeDetailed(root)
insert_Duplicate(root)
print("Break new Tree has been formed right here")
printTreeDetailed(root)
