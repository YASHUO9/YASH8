preorder = [1,2,4,5,3,6,7]
inOrder  = [4,2,5,1,6,3,7]

""""It is made by myself only."""""
# def making_Tree(preorder,inOrder):
#     root = preorder[0]
#     i = 0
#     for k in range(0,len(inOrder)-1):
#         if inOrder[k] == root:
#             print(i)
#             break
#         i+=1
        
#     left = i-1

#     left_content = []
#     right_content = []
#     count =0
#     for l in inOrder:
#         left_content.append(l)
#         if count == i-1:
#             break
#         count+=1
#     k = i+1
#     for li in range(k,len(inOrder)):
#         right_content.append(inOrder[li])   
#     print(left_content)
#     print(right_content)

# def join(left,right):
#     pass
    
# def printTreeDetailed(root):
#     if root == None:
#         return
#     print(root.data,end = ":")
#     if root.left != None:
#          print("L",root.left.data, end = " ,")
#     if root.right!= None:
#         print("R",root.right.data,end = "" ) 
#     print()
#     printTreeDetailed(root.left)
#     printTreeDetailed(root.right)



# class BinaryTreeNode:
#     def __init__(self,data):
#         self.data = data
#         self.left = None
#         self.right = None
        
# def join(left,right,root):
#     if root == None:
#         return
#     root = left[1]
#     q = BinaryTreeNode(root)
#     left_side = join
        

# making_Tree(preorder,inOrder)


#"""It is made by the Sir only""""

pre = [1,2,4,5,3,6,7]
inOrder  = [4,2,5,1,6,3,7]
def buildTreeFromPreIn(pre,Inorder):
    if len(pre) == 0:
        return None
    rootData = pre[0]
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
    
    leftPreorder = pre[1:lenLeftSubtree+1]
    rightPreorder =  pre[lenLeftSubtree+1:]
    
    leftChild = buildTreeFromPreIn(leftPreorder ,leftInOrder)
    rightChild   = buildTreeFromPreIn(rightPreorder,rightInorder)
    
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
      
       
       
root = buildTreeFromPreIn(pre,inOrder)
printTreeDetailed(root)

