hoo = [4,5,2,6,7,3,1]
go = hoo[:len(hoo)]
#Starting is the gap and the 2nd one is original
print(go)





#In this program/code the Firstly i have come deep in the inorder and postOrder 
#1.This code is same as the universal.

post = [4,5,2,6,7,3,1]
inOrder  = [4,2,5,1,6,3,7]
def buildTreeFromPreIn(post,Inorder):
    if len(post) == 0:
        return None
    
    rootData = post[len(post)-1]
    root = BinaryTreeNode(rootData)
    rootIndexInOrder = -1
    for i in range(0,len(Inorder)):
        if Inorder[i] == rootData:
            rootIndexInOrder = i
            break
    if rootIndexInOrder == -1:
        return None
    leftInOrder  = Inorder[0:rootIndexInOrder]
    rightInorder = Inorder[rootIndexInOrder+1:]
    
    lenLeftSubtree = len(leftInOrder)
    
    leftPostorder = post[:lenLeftSubtree]
    rightPostorder =  post[lenLeftSubtree:len(post)-1]
    
    leftChild = buildTreeFromPreIn(leftPostorder ,leftInOrder)
    rightChild   = buildTreeFromPreIn(rightPostorder,rightInorder)
    
    root.left = leftChild
    root.right = rightChild
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
      
       
       
root = buildTreeFromPreIn(post,inOrder)
printTreeDetailed(root)