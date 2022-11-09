#--Currently it is not completed--#
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
    

def convert_to_array(array,root):
    length = int(len(array))-1
    mid = length -1
    Data = array[mid]
    if Data == -1:
        return None
    if length -1 ==0:
        data = array[0]
    
    root = BinaryTreeNode(Data)
    
    if root.left == None or root.right == None:
        return
    leftTree = convert_to_array(array,root.left)
    rightTree = convert_to_array(array,root.right)
    root.left = leftTree
    root.right = rightTree
    return root
array = [1,2,3,4,5,6,7]
root = None
root = convert_to_array(array,root)   
    
    