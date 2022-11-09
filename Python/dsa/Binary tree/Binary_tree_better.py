class BinaryTreeNodes:
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
    
btn1 = BinaryTreeNodes(1)
btn2 = BinaryTreeNodes(2)
btn3 = BinaryTreeNodes(3)
btn4 = BinaryTreeNodes(4)
btn5 = BinaryTreeNodes(5)
btn6 = BinaryTreeNodes(6)
btn7 = BinaryTreeNodes(7)
btn1.left = btn2
btn1.right = btn3
btn2.left = btn4
btn2.right = btn5
btn3.right = btn6
btn3.left = btn7

printTreeDetailed(btn1) 
