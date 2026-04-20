class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def safe_pop(self):
        if len(self.stack) == 0:
            print("Stack is empty, nothing to pop.")
            return None
        return self.stack.pop()

    def display(self):
        print(self.stack)



s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()

print(s.safe_pop())
print(s.safe_pop())
print(s.safe_pop())
print(s.safe_pop())
