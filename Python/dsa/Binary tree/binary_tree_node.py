class BinaryTreeNodes:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def printTree(root):
    if root == None:
        return
    print(root.data)
    print(root.left.data)
    print(root.right.data)
    
btn1 = BinaryTreeNodes(1)
btn2 = BinaryTreeNodes(5)
btn3 = BinaryTreeNodes(4)

btn1.left = btn3
btn1.right = btn2
printTree(btn1)