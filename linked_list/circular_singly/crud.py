class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def size(self):
        if not self.head:
            return 0

        list_len = 1
        temp = self.head

        while temp != self.tail:
            list_len += 1
            temp = temp.next

        return list_len

    def __iter__(self):
        temp = self.head

        while temp:
            yield temp

            if temp == self.tail:
                break

            temp = temp.next

    def append(self, val):
        new_node = Node(val)

        if self.head:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        else:
            new_node.next = new_node
            self.head = new_node
            self.tail = new_node

    def insert(self, val, index):
        depth = self.size()

        if not 0 <= index <= depth:
            raise Exception("Index out of range")

        new_node = Node(val)

        if index == 0:
            if self.head:
                new_node.next = self.head
                self.tail.next = new_node
            else:
                new_node.next = new_node
                self.tail = new_node
            self.head = new_node
        elif index == depth:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        else:
            cur_index = 1
            cur = self.head

            while cur_index != index:
                cur_index += 1
                cur = cur.next

            new_node.next = cur.next
            cur.next = new_node

    def index(self, val):
        temp = self.head
        index = 0

        while temp:
            if temp.val == val:
                return index
            if temp == self.tail:
                raise Exception("Value doesn't exist")
            temp = temp.next
            index += 1
        
        raise Exception("Value doesn't exist")

    def delete(self, index):
        depth = self.size()

        if not 0 <= index <= depth:
            raise Exception("Index out of range")

        if index == 0:
            if self.head == self.tail:
                self.head.next = None
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.tail.next = self.head
        else:
            cur_index = 1
            cur = self.head

            while index != cur_index:
                cur = cur.next
                cur_index += 1

            if cur_index == depth - 1:
                cur.next = self.head
                self.tail = cur
            else:
                cur.next = cur.next.next

    def clear(self):
        self.tail.next = None
        self.head = None
        self.tail = None


linked_list = LinkedList()
input_list = [2, 3]
# input_list = []

'''Append'''
for val in input_list:
    linked_list.append(val)

'''Insertion'''
linked_list.insert(0, 0)
linked_list.insert(4, 3)
linked_list.insert(1, 1)

'''Deletion'''
linked_list.delete(0)
linked_list.delete(1)
# linked_list.delete(2)

'''Find index'''
print('Index of 1 is', linked_list.index(1))
print('Index of 3 is', linked_list.index(3))
print('Index of 4 is', linked_list.index(4))

'''Clear Everything'''
linked_list.clear()

'''Traversal'''
for node in linked_list:
    print(node.val)

# '''Size'''
print('Size', linked_list.size())

# '''Head & Tail'''
print('Head', linked_list.head.val if linked_list.head else None)
print('Tail', linked_list.tail.val if linked_list.tail else None)
print('Next to Tail', linked_list.tail.next.val if linked_list.tail else None)
