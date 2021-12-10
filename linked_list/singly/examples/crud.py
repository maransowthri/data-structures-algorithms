class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        
        while node:
            yield node
            node = node.next
    
    @staticmethod
    def len(node):
        length = 0
        
        while node:
            node = node.next
            length += 1
        
        return length

    def append(self, val):
        if not self.head:
            self.head = Node(val)
            self.tail = Node(val)
        else:
            node = self.head
            while node.next:
                node = node.next
            new_node =  Node(val)
            node.next = new_node
            self.tail = new_node

    def insert(self, val, index):
        node_len = LinkedList.len(self.head)
        
        if not 0 <= index <= node_len:
            raise Exception('Index out of range')
        
        new_node = Node(val)
        
        if index == 0:
            new_node.next = self.head
            self.head = new_node

            if not self.tail:
                self.tail = new_node
        elif index == node_len:
            self.tail.next = new_node
            self.tail = new_node
        else:
            node = self.head
            cur_index = 1
        
            while not cur_index == index:
                node = node.next
                cur_index += 1
        
            temp = node.next
            node.next = new_node
            new_node.next = temp


linked_list = LinkedList()
input_list = []

'''Append'''
for val in input_list:
    linked_list.append(val)

'''Insertion'''
linked_list.insert(0, 0)
linked_list.insert(1, 1)
linked_list.insert(2, 2)
linked_list.insert(-1, 0)
linked_list.insert(3, 4)

'''Traverse'''
for node in linked_list:
    print(node.val)

'''Head & Tail Values'''
print('First', linked_list.head.val)
print('Last', linked_list.tail.val)