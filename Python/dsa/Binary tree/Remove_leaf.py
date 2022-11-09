def treeinput():
    element = int(input())
    if element  == -1:
        return None
    ele = BinaryTreeNode(element)
    leftTree = treeinput()
    rightTree = treeinput()
    ele.left = leftTree
    ele.right = rightTree
    return ele
    

def Remove_Leaf_Nodes(root):
    if root == None:
        return None
    if root.left == None and root.right == None:
        return None
    root.left = Remove_Leaf_Nodes(root.left)
    root.right = Remove_Leaf_Nodes(root.right)
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


root  = treeinput()
print("Original leaf:")
printTreeDetailed(root)
print("After the leaf remove:")
root = Remove_Leaf_Nodes(root)
printTreeDetailed(root)
