



from numpy import empty


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
    
 
def Root_to_Node_Path(search,root):
    list = []
    if root == None:
        return None
    if  root.data == search:
        return list.append(root.data)
    
    Root_to_Node_Path(search,root.left)
    if list is not empty:
        list.append(root.data)
        return
    Root_to_Node_Path(search,root.right)
    if list is not empty:
        list.append(root.data)
        return
    return None
    
    