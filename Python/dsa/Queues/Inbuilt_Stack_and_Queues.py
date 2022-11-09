import queue
# q = queue.Queue()
#In built Queues library in the Python module
# q.put(1)
# q.put(2)
# q.put(3)
# q.put(4)
# q.put(5)

# while not q.empty():
#     print(q.get())

q = queue.LifoQueue()#here lifo stand for "last in first out"
#This library is act as the Stack in the python module
q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.put(5)
while not q.empty():
    print(q.get())
#we can use the lifoQueue as also the list