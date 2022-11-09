#It has the time Complexity of O(n2)
#because the loop has been run in the n *n times to complete the required result
def printCurrentLevel(root,level):
    if root == None:
        return
    if level == 1:
        print(root.data , end = " ")
    elif level > 1:
        printCurrentLevel(root.left,level -1)
        printCurrentLevel(root.right , level -1)
    else:
        pass
    
def LevelOrderTransever(root,num):
    for i in range(1,num+1):
        printCurrentLevel(root,i)

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
printTreeDetailed(root)
num = int(input("Enter the value of the height of the binary Tree \n"))
LevelOrderTransever(root,num)

