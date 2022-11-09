#it is working as i thought
#PROCEDURE
#1#. Firstly i have created the Queues
#2#. Secondly i have put the root as it is in the Queues and after that i have putted the "Null"
# so that i can make the new line 
# This will  help in making the new line in the printing

#3#. I have used the while loop so that i can loop the Queues until it is Empty
 
#4#. I also have to make sure about the situation of left and the right side of the root.



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
        front = 0
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
    print("Its Working")
    if root == None:
        return
    q = Queues()
    q.enqueues(root)
    q.enqueues("Null")
    
    while not q.isEmpty():
        if root != None:
            a = q.dequeues()
            if a == "Null":
                print("\n")
                a = q.dequeues()
                print(a.data)
            else:
                print(a.data)
            if a.left !=None:
                q.enqueues(a.left)
            if a.right != None:
                q.enqueues(a.right)
                
        elif not q.isEmpty():
            q.enqueues("Null")
            
                
   
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
#This program i have taken the help of Apani Kakasha