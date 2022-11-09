



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
    if root == None:
        return None
    if  int(root.data) == int(search):
        app.append(root.data)
        return True 
    
    a = Root_to_Node_Path(search,root.left)
    if a == True:
        app.append(root.data)
        return True
    b = Root_to_Node_Path(search,root.right)
    if b == True:
        app.append(root.data)
        return True
    
    
    
    
root = treeInput()
printTreeDetailed(root) 
search = int(input("Enter the number to search in the Binary tree "))
app =[]
a = Root_to_Node_Path(search,root)

if a != None:
    print(app)
else:
    print(a)
    
    
    