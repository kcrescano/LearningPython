class Stack:
    def __init__(self):
        self.stack = []
    def 

(self, item):
        self.stack.append(item)
    def 

(self):
        return self.stack.pop()
    def 

(self):
        return str(self.stack[-1])
    
s = Stack()
s.push('Hello')
s.push('World')
print(s.peek())
