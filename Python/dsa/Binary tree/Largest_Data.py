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

def largest_data(root):
    if root == None:
        return -1
    left = largest_data(root.left)
    a = left
    right = largest_data(root.right)
    b = right
    if a>b and b>root.data:
        return a
    elif b >a and a >root.data:
        return b
    else:
        return root.data
    
root = treeInput()
printTreeDetailed(root)
print("largest:",largest_data(root))
