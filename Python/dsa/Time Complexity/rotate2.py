# Deque (Doubly Ended Queue) in Python is implemented using the module “collections“. Deque is preferred over a list in the cases where we need quicker append and pop operations from both the ends of the container, as deque provides an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity.
from collections import deque
ask  = int(input("Enter the rotating number:"))

Array = [1,2,3,4,5,6]

ok = deque(Array)

ok.rotate(-ask)

print(ok)

#O(n)