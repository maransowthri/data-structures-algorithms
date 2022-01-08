class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def pre_order(root):
    res = []
    dfs(root, res)
    return res


def dfs(root, res):
    if root:
        res.append(root.val)
        dfs(root.left, res)
        dfs(root.right, res)


def pre_order_iter(root):
    res = []
    stack = [root]

    while stack:
        node = stack.pop()
        if node:
            res.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
    
    return res


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
for val in pre_order(drinks):
    print(val)

print('')
print('Iterative')
for val in pre_order_iter(drinks):
    print(val)