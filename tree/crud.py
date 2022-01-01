class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self, level=0):
        val = ' ' * level + self.val + '\n'

        if self.left:
            val += self.left.__str__(level + 1)

        if self.right:
            val += self.right.__str__(level + 1)
        
        return val

    def add_left_child(self, node):
        self.left = node

    def add_right_child(self, node):
        self.right = node


tree = Tree('Drinks')
cold = Tree('Cold')
hot = Tree('Hot')
tree.add_left_child(cold)
tree.add_right_child(hot)
coke = Tree('Coke')
cola = Tree('Cola')
tea = Tree('tea')
coffee = Tree('Coffee')
cold.add_left_child(coke)
cold.add_right_child(cola)
hot.add_left_child(tea)
hot.add_right_child(coffee)
print(tree)