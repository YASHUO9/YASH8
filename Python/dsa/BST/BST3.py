def isBST3(root,min_range,max_range):
    if root == None:
        return True
    if root.data < min_range or root.data > max_range:
        return False
    
    left = isBST3(root.left,min_range,root.data -1)
    right = isBST3(root.right,root.data,max_range)
    
    return left and right
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
root = treeInput()   
print(isBST3(root,-10000,10000))
