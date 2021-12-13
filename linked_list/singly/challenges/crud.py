class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        temp = self.head
        while temp:
            yield temp
            temp = temp.next

    def size(self):
        ll_len = 0
        temp = self.head

        while temp:
            ll_len += 1
            temp = temp.next

        return ll_len

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
            raise Exception("Index out of range")

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
            temp = self.head
            cur_index = 1

            while index != cur_index:
                cur_index += 1
                temp = temp.next

            new_node.next = temp.next
            temp.next = new_node


linked_list = LinkedList()
input_list = [0, 1, 2, 4]

for val in input_list:
    linked_list.append(val)

linked_list.insert(3, 3)
linked_list.insert(5, 5)

for node in linked_list:
    print(node.val)
