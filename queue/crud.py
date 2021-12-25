class Queue:
    def __init__(self):
        self.data = []
    
    def __str__(self):
        values = map(str, self.data)
        return ' <- '.join(values)
    
    def enque(self, val):
        self.data.append(val)
    
    def deque(self):
        return self.data.pop(0)
    
    def peek(self):
        return self.data[0]
    
    def is_empty(self):
        return self.data == []
    
    def clear(self):
        self.data = None


queue = Queue()
queue.enque(0)
queue.enque(1)
queue.enque(2)
queue.enque(3)
print('queue: ')
print(queue)
print('dequeing', queue.deque())
print('queue: ')
print(queue)
print('Peeked data', queue.peek())
print('Clearing out')
queue.clear()
print('queue is empty' if queue.is_empty() else 'queue is not empty')