class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop()
    def peek(self):
        return str(self.stack[-1])
    
s = Stack()
s.push('Hello')
s.push('World')
print(s.peek())
