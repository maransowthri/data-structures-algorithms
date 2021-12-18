from random import randint


class Node:
    def __init__(self, val, next=None, prev=None) -> None:
        self.val = val
        self.prev = prev
        self.next = next
    
    def __str__(self) -> str:
        return str(self.val)


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def __iter__(self):
        cur = self.head

        while cur:
            yield cur
            cur = cur.next
    
    def __str__(self) -> str:
        values = [str(node.val) for node in self]
        return ' -> '.join(values)
    
    def __len__(self) -> int:
        length = 0
        cur = self.head

        while cur:
            length += 1
            cur = cur.next
        
        return length
    
    def append(self, val):
        new_node = Node(val)

        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
    
    def generate(self, length, min, max):
        for _ in range(length):
            self.append(randint(min, max))