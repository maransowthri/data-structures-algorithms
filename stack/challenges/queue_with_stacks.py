class Stack:
    def __init__(self):
        self.data = []
    
    def push(self, val):
        self.data.append(val)
    
    def pop(self):
        return self.data.pop()

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return ' <- '.join(map(str, self.data))

class Queue:
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()
    
    def __str__(self):
        return str(self.in_stack)
    
    def enque(self, val):
        self.in_stack.push(val)
    
    def deque(self):
        while len(self.in_stack):
            self.out_stack.push(self.in_stack.pop())
        
        self.out_stack.pop()

        while len(self.out_stack):
            self.in_stack.push(self.out_stack.pop())


queue = Queue()
queue.enque(1)
queue.enque(2)
queue.enque(3)
queue.enque(4)
queue.deque()
queue.deque()
print(queue)