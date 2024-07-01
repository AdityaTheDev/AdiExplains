from collections import deque

# Initialize a deque
d = deque()

# Append elements to the right
d.append(1)
d.append(2)
d.append(3)

# Append elements to the left
d.appendleft(0)
d.appendleft(-1)

# Remove and return an element from the right
right_pop = d.pop()

# Remove and return an element from the left
left_pop = d.popleft()

# Print the deque
print(d)

# Print the popped elements
print(f'Popped from right: {right_pop}')
print(f'Popped from left: {left_pop}')

# Access elements by index
print(d[0])  # First element
print(d[-1]) # Last element

# Extend the deque with iterable
d.extend([4, 5, 6])
d.extendleft([-2, -3])

print(d)
