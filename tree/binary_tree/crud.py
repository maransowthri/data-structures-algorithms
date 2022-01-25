# Node
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Search element
def search(root, val):
    stack = [root]

    while stack:
        node = stack.pop(0)

        if node:
            if node.val == val:
                return True
            stack.append(node.left)
            stack.append(node.right)

    return False


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

if search(drinks, "Drinks"):
    print("Value exists")
else:
    print("Value doesn't exist")
