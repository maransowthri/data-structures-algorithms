class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        cur = self.head

        while cur:
            yield cur
            cur = cur.next

    def __str__(self):
        values = [str(node.val) for node in self]
        return ' <- '.join(values)

    def enque(self, val):
        node = Node(val)

        if self.head:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node

    def deque(self):
        val = self.head.val
        self.head = self.head.next

        if not self.head:
            self.tail = None
        
        return val

    def peek(self):
        return self.head.val

    def is_empty(self):
        return self.head is None

    def clear(self):
        self.head = None
        self.tail = None


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