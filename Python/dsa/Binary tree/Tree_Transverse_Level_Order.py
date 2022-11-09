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
def printTreeDetailed(root,count):#Post Order Traverse Tree
    if root == None:
        return
    print(root.data)
    if count == 1:
        c=0
        return c
    a = root.left
    b = root.right
    new = b
    before = 1
    while count == 0:
        num =2
        for i in range(0,num):
            if before == 1:
                p = printTreeDetailed(a,c+1)
                p
                q = printTreeDetailed(b,c+1)
                q
                a = a.left
                b = a.right
            if i ==2:
                before = 0
                a = new.left
                b = new.right
                num = 1
                
                
def print1(root,count):
    Game = True
    num = []
    while Game:
        if root == None:
            return
        print(root.data)
        if count == 1:
            return
        print1(root.left,count+1)
        print1(root.right,count+1)
        num.append(root.left)
        num.append(root.right)
        for i in num:
            print1(i,count)
        break
        
root = treeInput()
print1(root,0)

