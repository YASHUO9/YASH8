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
def printTreeDetailed(root):#Inorder Traverse Tree
    if root == None:
        return
    printTreeDetailed(root.left)
    print(root.data)
    printTreeDetailed(root.right)
    
    
    
root = treeInput()
printTreeDetailed(root)
