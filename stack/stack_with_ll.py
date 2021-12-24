class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

input_list = [0, 1, 2, 3, 4]
root = None

for val in input_list:
    root = Node(val, root)

cur = root

while cur:
    print(cur.val)
    cur = cur.next

print('Stack after pop: ')
root = root.next
cur = root

while cur:
    print(cur.val)
    cur = cur.next

print('Peeked data', root.val)
print('Peeked data', root.val)


print('Clearing out')
root = None
print('Stack is empty' if root is None else 'Stack is not empty')
