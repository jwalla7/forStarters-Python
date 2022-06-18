# class collections.deque([iterable[,maxlen]])

from collections import deque

# Returns a new deque object initialized left-to-right (using append()) with data from iterable.
#   If iterable is not specified, the new deque is empty.
#   Deques or Double Ended Queues are a generalization of stacks, and queues.
#   Deques support thread-safe, memory efficient appends and pops from either side
#     with approximately the same O(1) performance in either direction.

#  Deques are useful for tracking transactions and other pools of data where only
#    the most recent activity is of interest. De

#  https://docs.python.org/3/library/collections.html#deque-objects

queue_0 = deque()

queue_0.append(1)
queue_0.append(2)
queue_0.appendleft(3)
print(queue_0)

queue_0.pop()
print(queue_0)

queue_0.popleft()
print(queue_0)

queue_0.extend([2, 3, 4])
print(queue_0)

queue_0.extendleft([0, -1, -2, -3, -4])
print(queue_0)

# rotate(n=1)
#   Rotates the Deque n steps to the right. If n is negative, rotate to the left
#   When the deque is not empty, rotating one step to the right is equivalent to
#     queue_0.append(queue_0.popleft())


queue_0.rotate(1)  # Positive numbers swap n positions of right to the left
print(queue_0)
queue_0.rotate(-1)  # Negative numbers swap n positions of left to right
print(queue_0)
