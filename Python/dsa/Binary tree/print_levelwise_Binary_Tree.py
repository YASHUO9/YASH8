#print kth element of the binary tree

def printdepth(root,k):
    if root == None:
        return -1
    if k == 0:
        if root.left != None and root.right ==None:
            print(f"{root.data}:L{root.left.data},R  ")
        if root.left == None and root.right != None:
            print(f"{root.data}:L ,R{root.right.data}")
        if root.left != None and root.right != None:
            print(f"{root.data}:L{root.left.data},R{root.right.data}")
        if root.left == None and root.right == None:
            print(f"{root.data}:L  ,R  ")
    printdepth(root.left,k-1)
    printdepth(root.right,k-1)
    
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
    
#self made treeinput():
# in above
class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def printTreeDetailed(root):
    if root == None:
        return None
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
    

root  = treeinput()

for i in range(0,height(root)+1):
    printdepth(root,i)
