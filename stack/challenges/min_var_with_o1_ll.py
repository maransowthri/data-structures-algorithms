class Stack:
    def __init__(self):
        self.data = []
        self.min = []
    
    def __str__(self):
        return ' <- '.join(map(str, self.data))

    def get_min(self):
        return self.min[-1]

    def push(self, val):
        if len(self.data) != 0 and self.min[-1] < val:
            self.min.append(self.min[-1])
        else:
            self.min.append(val)

        self.data.append(val)
    
    def pop(self):
        self.min.pop()
        self.data.pop()


stack = Stack()
stack.push(4)
stack.push(1)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(0)
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
print(stack)
print(stack.get_min())