class Stack:
    def __init__(self):
        self.data = []
    
    def __str__(self):
        values = reversed(self.data)
        values = list(map(str, values))
        return '\n'.join(values)

    def is_empty(self):
        return self.data == []
    
    def push(self, val):
        self.data.append(val)

    def pop(self):
        return self.data.pop()
    
    def peek(self):
        return self.data[-1]
    
    def clear(self):
        self.data.clear()

stack = Stack()
stack.push(0)
stack.push(1)
stack.push(2)
stack.push(3)
print('Stack: ')
print(stack)
stack.pop()
print('Stack: ')
print(stack)
print('Peeked data', stack.peek())
print('Clearing out')
stack.clear()
print('Stack is empty' if stack.is_empty() else 'Stack is not empty')