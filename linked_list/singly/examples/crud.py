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

    def size(self):
        length = 0
        node = self.head
        while node:
            node = node.next
            length += 1

        return length

    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def insert(self, val, index):
        node_len = self.size()

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

            new_node.next = node.next
            node.next = new_node

    def index(self, val):
        temp = self.head
        cur_index = 0
        while temp:
            if temp.val == val:
                return cur_index
            else:
                cur_index += 1
                temp = temp.next
        raise Exception('Value doesn"t exist')

    def delete(self, index):
        node_len = self.size()

        if node_len == 0 or not 0 <= index < node_len:
            raise Exception('Index out of range')

        if index == 0:
            self.head = self.head.next

            if not self.head:
                self.tail = None
        else:
            temp = self.head
            cur_index = 0

            while cur_index != index:
                prev = temp
                temp = temp.next
                cur_index += 1

            prev.next = temp.next

            if not temp.next:
                self.tail = prev

    def clear(self):
        self.head = None
        self.tail = None


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

'''Size'''
print('Size', linked_list.size())

'''Finding index'''
print('Index of 0 is', linked_list.index(0))
# print('Index of 8 is', linked_list.index(8))

'''Deletion'''
linked_list.delete(1)
linked_list.delete(0)
linked_list.delete(2)
# linked_list.delete(0)
# linked_list.delete(0)

linked_list.clear()

'''Traverse'''
for node in linked_list:
    print(node.val)

'''Head & Tail Values'''
print('First', linked_list.head.val if linked_list.head else None)
print('Last', linked_list.tail.val if linked_list.tail else None)