class PowerOfTwo():

    def __init__(self, max):
        self.max = max
        self.number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if(self.number <= self.max):
            squarePower = self.number ** 2
            self.number += 1
            return squarePower
        else:
            self.number = 0
            raise StopIteration

power2 = PowerOfTwo(5)

for i in power2:
    print(i)
