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

def numNodes(root):
    if root == None:
        return 0
    leftCount = numNodes(root.left)
    rightCount = numNodes(root.right)
    #if we remove the 1 from here then the number of nodes will become 0"
    
    return 1+ leftCount + rightCount
def sum(root):
    if root == None:
        return 0
    leftCount = sum(root.left)
    rightCount = sum(root.right)
    
    return root.data + leftCount +rightCount
    
root = treeInput()
printTreeDetailed(root)
print(numNodes(root))
print("sum")
print(sum(root))
