#print kth element of the binary tree

def max(root):
    if root ==  None:
        return 0
    left_num = max(root.left)
    right_num = max(root.right)
    if left_num > right_num and left_num > root.data:
        return left_num
    elif right_num > left_num and right_num > root.data:
        return right_num
    elif root.data > left_num and root.data > right_num:
        return root.data
    else:
        pass
def mini(root):
    if root ==  None:
        return 100000
    left_num = mini(root.left)
    right_num = mini(root.right)
    if left_num < right_num and left_num < root.data:
        return left_num
    elif right_num < left_num and right_num < root.data:
        return right_num
    elif root.data < left_num and root.data < right_num:
        return root.data
    else:
        pass
    
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
print("minimum Node is ::",end = "")
print(mini(root))
print("maximum Node is ::" , end = "")
print(max(root))
