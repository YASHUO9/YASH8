#print kth element of the binary tree

def printdepth(root,k,d =0):
    if root == None:
        return
    if k == d:
        print(root.data)
        return
    printdepth(root.left,k,d+1)
    printdepth(root.right,k,d+1)
    
    
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
    
#copy
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
printdepth(root,2)
