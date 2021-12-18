from base import LinkedList


class SinglyList(LinkedList):
    def __init__(self):
        super().__init__()
    
    def remove_duplicates(self):
        values = {self.head.val} if self.head else set()
        cur = self.head

        while cur.next:
            if cur.next.val in values:
                cur.next = cur.next.next
            else:
                values.add(cur.next.val)
                cur = cur.next
        
        self.tail = cur



linked_list = SinglyList()
linked_list.generate(100, 1, 5)
# input_list = [1, 2, 1, 3, 2, 1, 3, 5]

# for val in input_list:
#     linked_list.append(val)

linked_list.remove_duplicates()
print(linked_list)

print('First', linked_list.head.val if linked_list.head else None)
print('First', linked_list.tail.val if linked_list.tail else None)