from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, value):
        self.queue.append(value)

    def safe_dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty, cannot dequeue.")
            return None
        return self.queue.popleft()

    def display(self):
        print(list(self.queue))


q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

print(q.safe_dequeue())
print(q.safe_dequeue())
print(q.safe_dequeue())
print(q.safe_dequeue())
