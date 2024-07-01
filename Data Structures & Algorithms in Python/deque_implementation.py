class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def append(self, value):
        self.items.append(value)

    def appendleft(self, value):
        self.items.insert(0, value)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty deque")
        return self.items.pop()

    def popleft(self):
        if self.is_empty():
            raise IndexError("pop from an empty deque")
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty deque")
        return self.items[-1]

    def peekleft(self):
        if self.is_empty():
            raise IndexError("peek from an empty deque")
        return self.items[0]

    def size(self):
        return len(self.items)

# Example usage:
d = Deque()
d.append(1)
d.append(2)
d.appendleft(0)
print(d.items)  # Output: [0, 1, 2]

print(d.pop())      # Output: 2
print(d.popleft())  # Output: 0
print(d.items)      # Output: [1]

print(d.peek())     # Output: 1
d.append(3)
print(d.peekleft()) # Output: 1
print(d.size())     # Output: 2
