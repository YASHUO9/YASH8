#whose parents are not same at all are called sibling
#print kth element of the binary tree

def sibling(root):
    if root == None:
        return None
    leftroot = sibling(root.left)
    rightroot = sibling(root.right)
    if leftroot == 1 and rightroot!= 1:
        print("OP")
        print(root.data)
    elif rightroot == 1 and leftroot!= 1:
        print("OP")
        print(root.data)
    else:
        print("non zero")
        return 1
    
    
    
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
sibling(root)