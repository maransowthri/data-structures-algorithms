class CircularQueue:
    def __init__(self, size):
        self.data = [None] * size
        self.size = size
        self.start = -1
        self.top = -1

    def __str__(self):
        return ' <- '.join(map(str, self.data))

    def is_full(self):
        return self.top + 1 == self.start or (self.start == 0 and self.top == self.size - 1)

    def is_empty(self):
        return self.top == -1

    def enque(self, val):
        if not self.is_full():
            if self.top == self.size - 1:
                self.top = 0
            else:
                self.top += 1

            if self.start == -1:
                self.start = 0

            self.data[self.top] = val
            return "Enqued successfully"
        else:
            return "Queue is full"

    def deque(self):
        start = self.start
        
        if self.is_empty():
            return "Queue is empty"
        elif self.start == self.size - 1:    
            self.start = 0
        else:
            self.start += 1
        
        first = self.data[start]
        self.data[start] = None
        
        return first
    
    def peek(self):
        return self.data[self.start]
    
    def clear(self):
        self.data = [None] * self.size
        self.start = -1
        self.top = -1

queue = CircularQueue(5)
print(queue)
print('Is full?', queue.is_full())
print('Is empty?', queue.is_empty())
queue.enque(0)
queue.enque(1)
queue.enque(2)
queue.enque(3)
queue.enque(4)
print(queue)
queue.deque()
print(queue)
print(queue.enque(5))
print(queue)
print('Peeked', queue.peek())
queue.clear()
print('Empty', queue.is_empty())