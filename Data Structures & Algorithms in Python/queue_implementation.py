class Queue:
    def __init__(self):
        # Initialize an empty list to store the queue items.
        self.items = []

    def is_empty(self):
        # Check if the queue is empty.
        return len(self.items) == 0

    def enqueue(self, item):
        # Add an item to the end of the queue.
        self.items.append(item)

    def dequeue(self):
        # Remove and return the item from the front of the queue.
        # Raise an error if the queue is empty.
        if self.is_empty():
            raise IndexError("Can't dequeue as the queue is empty")
        return self.items.pop(0)

    def front(self):
        # Return the front item of the queue without removing it.
        # Raise an error if the queue is empty.
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]

    def size(self):
        # Return the number of items in the queue.
        return len(self.items)
    
    def print_queue(self):
        # Print the queue elements
        print("Queue:", " -> ".join(map(str, self.items)))


if __name__ == "__main__":
    
    q=Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.print_queue()
    print("Front element :",q.front())
    print("Size of the queue :",q.size())
    q.dequeue()
    q.print_queue()
    print("Front element :",q.front())
    
    
