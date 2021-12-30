class StackSet:
    def __init__(self, size):
        self.staks = []
        self.size = size

    def __str__(self):
        return ' <- '.join(list(map(str, self.staks)))
    
    def push(self, val):
        if len(self.staks) and len(self.staks[-1]) < self.size:
            self.staks[-1].append(val)
        else:
            self.staks.append([val])
    
    def pop(self):
        if self.staks == []:
            raise Exception('Stack is empty')
        else:
            val = self.staks[-1].pop()

            if self.staks[-1] == []:
                self.staks.pop()

            return val
    
    def pop_at(self, index):
        if 0 <= index < len(self.staks):
            return self.staks[index].pop()
        else:
            raise Exception('Index does not exist')


stackSets = StackSet(3)
stackSets.push(0)
stackSets.push(1)
stackSets.push(2)
stackSets.push(3)
stackSets.push(4)
stackSets.push(5)
stackSets.push(6)
print(stackSets)
stackSets.pop()
stackSets.pop()
stackSets.pop()
stackSets.pop()
print(stackSets)
stackSets.push(3)
stackSets.push(4)
stackSets.push(5)
stackSets.push(6)
print(stackSets)
stackSets.pop_at(1)
print(stackSets)
stackSets.pop()
stackSets.pop()
stackSets.pop()
print(stackSets)