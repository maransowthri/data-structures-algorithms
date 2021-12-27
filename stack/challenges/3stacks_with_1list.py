class Stack:
    def __init__(self, data):
        self.data = data
        self.top = -1

    def push(self, val):
        if self.top == -1:
            self.data[0] = val
            self.top = 0
        elif self.top == len(self.data) - 1:
            raise Exception('Stack is full')
        else:
            self.top += 1
            self.data[self.top] = val
    
    def pop(self):
        if self.top == -1:
            raise Exception('Stack is empty')
        elif self.top == 0:
            val = self.data[0]
            self.data[0] = None
            self.top = -1
            return val
        else:
            val = self.data[self.top]
            self.data[self.top] = None
            self.top -= 1
            return val
    
    def peek(self):
        return self.data[-1]
    
    def is_full(self):
        return self.top == len(self.data) - 1

    def is_empty(self):
        return self.top == - 1

    def __str__(self):
        return ' -> '.join(list(map(str, self.data)))

        
class Stacks:
    def __init__(self, size):
        self.data = [None for _ in range(size * 3)]
        self.size = size
        self.stack_a = Stack(self.data[:self.size])
        self.stack_b = Stack(self.data[self.size: 2 * self.size])
        self.stack_c = Stack(self.data[2 * self.size:])

print()
stacks = Stacks(3)
stacks.stack_a.push(1)
stacks.stack_a.push(2)
stacks.stack_a.push(3)
print('Stack A', stacks.stack_a)
print('Is Stack A full?', stacks.stack_a.is_full())
print('Peeked Stack A', stacks.stack_a.peek())
print('Popped Stack A', stacks.stack_a.pop())
print('Stack A', stacks.stack_a)
# stacks.stack_a.push(4)
stacks.stack_b.push(1)
print('Stack B', stacks.stack_b)
print('Is Stack B full?', stacks.stack_b.is_full())
print('Is Stack B empty?', stacks.stack_b.is_empty())
print('Stack C', stacks.stack_c)
print('Is Stack C empty?', stacks.stack_c.is_empty())
