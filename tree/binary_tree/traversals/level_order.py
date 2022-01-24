import queue


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root):
    if root:
        queue = [root]

        while queue:
            node = queue.pop(0)

            if node:
                yield node.val
                queue.append(node.left)
                queue.append(node.right)


drinks = Node('Drinks')
hot = Node('Hot')
cold = Node('Cold')
drinks.left = hot
drinks.right = cold
tea = Node('Tea')
coffee = Node('Coffee')
hot.left = tea
hot.right = coffee
slize = Node('Slize')
maaza = Node('Maaza')
cold.left = slize
cold.right = maaza

print('Recursive')
for val in level_order(drinks):
    print(val)
