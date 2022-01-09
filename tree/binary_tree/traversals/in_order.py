class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def in_order(root):
    res = []
    dfs(root, res)
    return res

def dfs(root, res):
    if root:
        dfs(root.left, res)
        res.append(root.val)
        dfs(root.right, res)

def in_order_iter(root):
    res = []
    stack = []

    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            node = stack.pop()
            res.append(node.val)
            root = node.right
    
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
for val in in_order(drinks):
    print(val)

print('')
print('Iterative')
for val in in_order_iter(drinks):
    print(val)