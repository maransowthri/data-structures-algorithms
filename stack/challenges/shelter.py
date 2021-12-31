class Shelter:
    def __init__(self):
        self.data = []

    def __str__(self):
        return ' <- '.join(self.data)

    def enque(self, animal):
        self.data.append(animal.strip().lower())
    
    def deque(self, val=None):
        if val:
            val = val.strip().lower()
            if val in self.data:
                self.data.remove(val)
                return val
            else:
                return "Animal does not exist"
        else:
            val = self.data[0]
            self.data = self.data[1:]
            return val


shelter = Shelter()
shelter.enque('Dog')
shelter.enque('Dog')
shelter.enque('Dog')
shelter.enque('Cat')
shelter.enque('Cat')
shelter.enque('Snake')
shelter.deque()
shelter.deque()
shelter.deque('Cat')
shelter.deque('Cat')
# shelter.deque()
# shelter.deque()
print(shelter)