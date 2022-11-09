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
    
def main_work(root):
    left = Diameter_BinaryTree(root.left)
    right = Diameter_BinaryTree(root.right)
    if left == right :
        element_in_right = int(right_element(root)) -1
        print(2*element_in_right)
        return
    else:
        print(diameter(root))
        return
#if left > right tree
def left_Tree(root):
    if root == None:
        return 0
    left = left_Tree(root.left)
    right = left_Tree(root.right)
    if left  == 0 and right != 0 or right == 0 and left != 0 or left != 0 and right !=0:
        return left +right +1
    else:
        print(diameter(root))
        
#if right tree = left tree then 
def Diameter_BinaryTree(root):
    if root == None:
        return 0
    left_tree = Diameter_BinaryTree(root.left)
    right_tree = Diameter_BinaryTree(root.right)
    return left_tree + right_tree +1


#To find the right element
def right_element(root):
    if root == None:
        return 0
    right_tree = Diameter_BinaryTree(root.right)
    return right_tree +1

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

def height(root):
    if root == None:
        return 0
    return 1 +max(height(root.left),height(root.right))
def diameter(root):
    if root == None:
        return 0
    option1 = height(root.left) +height(root.right)
    option2 = diameter(root.left)
    option3 = diameter(root.right)
    return max(option1,max(option2,option3))
root  = treeinput()
main_work(root)

