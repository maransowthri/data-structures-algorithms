class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        cur = self.head

        while cur:
            yield cur
            if cur == self.tail:
                break
            cur = cur.next
    
    def size(self):
        node_len = 0
        cur = self.head

        while cur:
            node_len += 1
            if cur == self.tail:
                break
            cur = cur.next
        
        return node_len

    def reverse(self):
        cur = self.tail

        while cur:
            yield cur
            if cur == self.head:
                break
            cur = cur.prev
    
    def append(self, val):
        new_node = Node(val)

        if self.head:
            new_node.prev = self.tail
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node
            self.head.prev = self.tail
        else:
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
            self.tail = new_node

    def insert(self, index, val):
        new_node = Node(val)

        if not self.head:
            new_node.prev = new_node
            new_node.next = new_node
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.prev = self.tail
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.tail.next = new_node
        elif index >= self.size():
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node
            self.head.prev = new_node
        else:
            cur_index = 1
            cur = self.head

            while cur_index < index:
                cur = cur.next
                cur_index += 1
            
            new_node.prev = cur
            new_node.next = cur.next
            cur.next.prev = new_node
            cur.next = new_node

    def index(self, val):
        if not self.head:
            raise Exception('List is empty')

        cur = self.head
        index = 0

        while cur:
            if cur.val == val:
                return index
            if cur == self.tail:
                break
            index += 1
            cur = cur.next
        
        raise Exception('Value does not exist')

    def pop(self, index):
        depth = self.size()

        if not self.head:
            raise Exception('List is empty')
        elif 0 <= index < depth:
            if index == 0:
                if depth == 1:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif index == depth - 1:
                self.tail = self.tail.prev
                self.tail.next = self.head
                self.head.prev = self.tail
            else:
                cur_index = 0
                cur = self.head
                
                while cur_index < index:
                    cur = cur.next
                    cur_index += 1
                
                cur.prev.next = cur.next
                cur.next.prev = cur.prev                
        else: 
            raise Exception('Index out of range')

    def clear(self):
        cur = self.head
        self.tail.next = None
        self.head = None
        self.tail = None

        while cur.prev:
            cur.prev = None
            cur = cur.next


linked_list = LinkedList()
input_list = []
input_list = [1, 3, 4]

'''Append'''
for val in input_list:
    linked_list.append(val)

'''Insertion'''
linked_list.insert(0, 0)
linked_list.insert(2, 2)
linked_list.insert(5, 5)

'''Search'''
print('Index of 0 is', linked_list.index(0))
print('Index of 2 is', linked_list.index(2))
print('Index of 5 is', linked_list.index(5))
# print('Index of value that does not exist is', linked_list.index(8))

'''Deletion'''
linked_list.pop(0)
linked_list.pop(2)
linked_list.pop(3)

'''Clear'''
linked_list.clear()

'''Traverse'''
print('Traverse')
for node in linked_list:
    print(node.val)

'''Reversal'''
print('Reversal')
for node in linked_list.reverse():
    print(node.val)

'''Size'''
print('Size', linked_list.size())

'''Head & Tail Values'''
print('First', linked_list.head.val if linked_list.head else None)
print('First from Last', linked_list.tail.next.val if linked_list.tail else None)
print('Last', linked_list.tail.val if linked_list.tail else None)
print('Last from First', linked_list.head.prev.val if linked_list.head else None)