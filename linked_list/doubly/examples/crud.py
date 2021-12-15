class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        cur = self.head

        while cur:
            yield cur
            cur = cur.next

    def size(self):
        node_len = 0
        cur = self.head

        while cur:
            node_len += 1
            cur = cur.next

        return node_len

    def reverse(self):
        cur = self.tail

        while cur:
            yield cur
            cur = cur.prev

    def index(self, val):
        if not self.head:
            raise Exception('Linked list does not exist')

        cur_index = 0
        cur = self.head

        while cur:
            if cur.val == val:
                return cur_index
            cur = cur.next
            cur_index += 1

        raise Exception('Value not exist')

    def append(self, val):
        new_node = Node(val)

        if self.head:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def insert(self, val, index):
        head_size = self.size()

        if not 0 <= index <= head_size:
            raise Exception("Index out of range")

        new_node = Node(val)

        if index == 0:
            if self.head:
                new_node.next = self.head
                self.head.prev = new_node
            else:
                self.tail = new_node
            self.head = new_node
        elif index == head_size:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            cur_index = 1
            cur = self.head

            while index != cur_index:
                cur_index += 1
                cur = cur.next

            new_node.prev = cur
            new_node.next = cur.next
            cur.next.prev = new_node
            cur.next = new_node

    def pop(self, index):
        head_size = self.size()

        if not 0 <= index < head_size:
            raise Exception("Index out of range")

        if not self.head:
            raise Exception("List is empty")

        if index == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
        else:
            cur_index = 0
            cur = self.head

            while cur_index < index:
                cur_index += 1
                prev = cur
                cur = cur.next

            if cur_index == head_size - 1:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                prev.next = cur.next
                cur.next.prev = prev

            cur.next = None
            cur.prev = None

    def clear(self):
        if not self.head:
            raise Exception("List does not exist")

        cur = self.head

        while cur:
            cur.prev = None
            cur = cur.next

        self.head = None
        self.tail = None


linked_list = LinkedList()
input_list = []
input_list = [1, 3]

'''Append'''
for val in input_list:
    linked_list.append(val)

'''Insertion'''
linked_list.insert(0, 0)
linked_list.insert(4, 3)
linked_list.insert(2, 2)

'''Searching'''
print('Index of 0 is', linked_list.index(0))
# print('Index of 4 is', linked_list.index(4))
# print('Index of 8 is', linked_list.index(8))

'''Removal'''
linked_list.pop(0)
linked_list.pop(1)
linked_list.pop(2)

'''Clear'''
linked_list.clear()

'''Traversal'''
print('Traversal')
for node in linked_list:
    print(node.val)

'''Reversal'''
print('Reversal')
for node in linked_list.reverse():
    print(node.val)

'''Head & Tail Values'''
print('First', linked_list.head.val if linked_list.head else None)
print('Last', linked_list.tail.val if linked_list.tail else None)
