from base import LinkedList
from base import Node

def intersection(ll1, ll2):
    if not ll1.tail == ll2.tail:
        raise Exception("Not intersecting")
    
    len_ll1 = len(ll1)
    len_ll2 = len(ll2)
    longer = ll1.head if len_ll1 > len_ll2 else ll2.head
    shorter = ll2.head if len_ll1 > len_ll2 else ll1.head
    diff = abs(len_ll1 - len_ll2)

    while diff:
        longer = longer.next
        diff -= 1
    
    while shorter != longer:
        shorter = shorter.next
        longer = longer.next

    return shorter

def append(ll1, ll2, val):
    new_node = Node(val)
    ll1.tail.next = new_node
    ll1.tail = new_node
    ll2.tail.next = new_node
    ll2.tail = new_node


ll1 = LinkedList()
ll1.generate(6, 1, 99)

ll2 = LinkedList()
ll2.generate(5, 1, 99)

append(ll1, ll2, 5)
append(ll1, ll2, 7)
append(ll1, ll2, 11)

print(ll1)
print(ll2)

print(intersection(ll1, ll2))
