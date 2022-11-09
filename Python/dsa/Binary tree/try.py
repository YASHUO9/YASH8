

from queue import Queue

q = Queue()
print(q.qsize())
q.put('1')
print("\nFull: ", q.full())
print("\nElements dequeued from the queue")
print(q.get())
print("\nEmpty: ", q.empty())
q.put(1)
