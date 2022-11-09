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

def height(root):
    if root == None:
        return 0
    leftCount = height(root.left) +1
    rightCount = height(root.right)+1
    
    if leftCount >rightCount:
        return leftCount
    else:
        return rightCount
    
    
root = treeInput()
printTreeDetailed(root)
print("height of tree")
print(height(root))