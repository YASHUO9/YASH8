def treeInput():
    rootData = int(input())
    if rootData == -1:
        return None
    
    root = BinaryTreeNode(rootData)
    leftTree = treeInput()
    rightTree = treeInput()
    root.left = leftTree
    root.right = rightTree
    return root

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

def Search(root,x):
    if root == None:
        print("NULL")
        return 
    if root.data == x:
        print("PRESENT")
        return 
    if root.data >x:
        Search(root.left,x)   
    else:
        Search(root.right,x)
#we are giving the input tree as root.right >root.left and root .data >root.right.data 
##--- Right--side--is--greater--than--all
root = treeInput()
printTreeDetailed(root)
ask = int(input("Enter the number to search in the Binary tree\n"))
Search(root,ask)