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
    
def height(root):
    if root == None:
        return 0
    return 1 + max(height(root.left),height(root.right))

def isBalanced(root):
    if root == None:
        return True
    lh = height(root.left)
    rh = height(root.right)
    
    if lh -rh >1 or rh - lh>1:
        return False
    isLeftBalanced = isBalanced(root.left)
    isRightBalanced = isBalanced(root.right)
    
    if isLeftBalanced and isRightBalanced :
        return True
    else:
        return False

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
printTreeDetailed(root)
print(isBalanced(root))
