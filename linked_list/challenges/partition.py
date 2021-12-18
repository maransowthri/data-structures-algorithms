from base import LinkedList

    
def partition(ll, val):
    cur = ll.head
    ll.tail = ll.head

    while cur:
        next_node = cur.next
        cur.next = None
        if cur.val < val:
            cur.next = ll.head
            ll.head = cur
        else:
            ll.tail.next = cur
            ll.tail = cur
        cur = next_node


linked_list = LinkedList()
input_list = [11, 3, 9, 10, 15]

for val in input_list:
    linked_list.append(val)

print(linked_list)
partition(linked_list, 10)
print(linked_list)
