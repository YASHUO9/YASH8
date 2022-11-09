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

def Number_of_leaf_Node(root):
    if root == None:
        return 0.5
    leftCount = Number_of_leaf_Node(root.left) 
    rightCount = Number_of_leaf_Node(root.right)
    return leftCount + rightCount
    
    
    
root = treeInput()
printTreeDetailed(root)
print("leaf Node count of tree : ",end="")
print(Number_of_leaf_Node(root))