class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Stack:
    def __init__(self):
        self.top = None
        self.min = None

    def push(self, val):
        if self.min and val > self.min.val:
            self.min = Node(self.min.val, self.min)
        else:
            self.min = Node(val, self.min)
        self.top = Node(val, self.top)

    def pop(self):
        if self.top:
            self.top = self.top.next
            self.min = self.min.next
        else:
            raise Exception('Node is empty')

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(0)
stack.push(4)
stack.pop()
stack.pop()
stack.pop()
stack.pop()
print(stack.min.val)