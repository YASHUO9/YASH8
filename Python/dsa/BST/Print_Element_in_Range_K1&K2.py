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
    
def element_range(root,k1,k2):
    if root == None:
        return 0
    if k1 <= root.data and k2 >= root.data:
        print(root.data)
    if k1 > root.data:
        element_range(root.right,k1,k2)
    elif k2 <root.data:
        element_range(root.left,k1,k2)
    else:
        pass
    
root = treeInput()
printTreeDetailed(root)
element_range(root,12,100)