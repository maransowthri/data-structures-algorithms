from base import LinkedList


class SinglyList(LinkedList):
    def __init__(self):
        super().__init__()
    
    def get(self, index):
        head_size = len(self)

        if not -head_size <= index < head_size:
            raise Exception('Index out of range')

        cur_index = 0
        cur = self.head

        while cur_index != index and cur_index - head_size != index :
            cur = cur.next
            cur_index += 1
        
        return cur


linked_list = SinglyList()
linked_list.generate(10, 1, 99)
print(linked_list)
print(linked_list.get(-1))
    