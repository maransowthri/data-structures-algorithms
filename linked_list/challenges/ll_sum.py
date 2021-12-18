from base import LinkedList


def ll_sum(l1, l2):
    carry = 0
    cur1 = l1.head
    cur2 = l2.head
    out_ll = LinkedList()

    while cur1 or cur2 or carry:
        res = carry
        if cur1:
            res += cur1.val
            cur1 = cur1.next
        if cur2:
            res += cur2.val
            cur2 = cur2.next
        out_ll.append(res % 10)
        carry = res // 10
    
    return out_ll

linked_list1 = LinkedList()
linked_list2 = LinkedList()
input_list1 = [7, 1, 8]
input_list2 = [5, 9, 2]

for val in input_list1:
    linked_list1.append(val)

print(linked_list1)

for val in input_list2:
    linked_list2.append(val)

print(linked_list2)
print(ll_sum(linked_list1, linked_list2))
