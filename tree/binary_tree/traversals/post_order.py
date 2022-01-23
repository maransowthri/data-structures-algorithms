class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def post_order(root):
    res = []
    dfs(root, res)
    return res


def dfs(root, res):
    if root:
        dfs(root.left, res)
        dfs(root.right, res)
        res.append(root.val)


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
for val in post_order(drinks):
    print(val)