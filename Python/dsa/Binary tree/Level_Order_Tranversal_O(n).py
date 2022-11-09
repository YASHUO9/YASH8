
class Queues:
    def __init__(self):
        self.data= []
        self.count = 0
        self.num = 1
    def enqueues(self,item):
        self.data.append(item)
        self.count = self.count +1
    def dequeues(self):
        if self.isEmpty():
            print("Hey! Stack is Empty!!")
            return
        self.count = self.count -1
        front =0
        return self.data.pop(front)
    def size(self):
        return self.count
    def isEmpty(self):
        return self.size() == 0
    def front(self):
        if self.isEmpty():
            print("Hey! Stack is Empty!!")
            return
        return self.data[self.count-1]
    


def LOT(root):
    
    q = Queues()
    q.enqueues(root.data)
    
    while not q.isEmpty():
        node_curr = q.dequeues()
        print(node_curr.data)
        if root.left != None:
            q.enqueues(root.left)
        if root.right != None:
            q.enqueues(root.right)
   
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
LOT(root)