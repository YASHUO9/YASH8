import queue
#inbuilt queue
# This is not using the same method as that of in Stack
q = queue.Queue()
q.put(1)
q.put(2)
q.put(3)

while not q.empty():
    print(q.get())



#It is similar as the Stack in the module queue
q1 = queue.LifoQueue()
q1.put(1)
q1.put(3)
q1.put(44)
while not q1.empty():
    print(q1.get())








