#this code is an example of how to create constructor class that is iterable

class Test:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self  # The object itself is an iterator.

    def __next__(self):
        if self.current < self.n:
            self.current += 1
            return self.current
        else:
            raise StopIteration

# Usage example
t = Test(4)
print(t.n)
for i in t:
    print(i)
