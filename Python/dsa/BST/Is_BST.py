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
    
def minTree(root):
    if root == None:
        return 1000000
    leftmin = minTree(root.left)
    rightmin = minTree(root.right)
    return min(leftmin,rightmin,root.data)
def maxTree(root):
    if root == None:
        return -100000
        leftmax = maxTree(root.left)
        rightmax = maxTree(root.right)
        return max(leftmax,rightmax,root.data)
    
def isBST(root):
    if root == None:
        return True
    
    leftmax = maxTree(root.left)
    rightmin = minTree(root.right)
    if root.data > rightmin or root.data <= leftmax:
        return False
    
    isleftBST = isBST(root.left)
    isrightBST = isBST(root.right)
    return isleftBST and isrightBST
        
root = treeInput()
isBST(root)