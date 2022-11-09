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
    
def path_sum_root_to_leaf(root,k,string):
    if root == None:
        return 0
    string.append(root.data)
    sum = 0
    for i in string:
        sum = sum + int(i)
    if sum == k:
        if root.left == None and root.right == None:
            print(string)
        
    left = path_sum_root_to_leaf(root.left,k,string)
    right = path_sum_root_to_leaf(root.right,k,string)
    if  root.left == None and root.right == None:
        #This will act when we are at leaf of the tree
        string.pop()
        return 0
    #This will acting when we are not  in the leaf but returning to the previous slide that's why i am deleting the one element each time.
    string.pop()

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
string = []
path_sum_root_to_leaf(root,12,string)

