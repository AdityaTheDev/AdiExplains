
class Node:
    def __init__(self, data):
        self.data = data  # Store data
        self.next = None  # Pointer to next node

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize head
        self.tail = self.head  # Initialize tail
        self.length = 0  # Initialize length

    def append(self, data):
        new_node = Node(data)  # Create new node
        if self.head == None:
            self.head = new_node  # Set head
            self.tail = self.head  # Set tail
            self.length = 1
        else:
            self.tail.next = new_node  # Link new node
            self.tail = new_node  # Update tail
            self.length += 1

    def prepend(self, data):
        new_node = Node(data)  # Create new node
        if self.head == None:
            self.head = new_node  # Set head
            self.tail = self.head  # Set tail
            self.length += 1
        else:
            new_node.next = self.head  # Link new node
            self.head = new_node  # Update head
            self.length += 1

    def print_list(self):
        if self.head == None:
            print("Empty")  # Check if list is empty
        else:
            current_node = self.head
            while current_node != None:
                print(current_node.data, end='->')  # Print data
                current_node = current_node.next  # Move to next node
        print()

    def insert(self, position, data):
        if position >= self.length:
            if position > self.length:
                print("This position is out of the linkedlist")
            self.append(data)
        elif position == 0:
              self.prepend(data)
        else:
            new_node = Node(data)
            current_node = self.head
            for i in range(position - 1):
                current_node = current_node.next  # Traverse to position
            new_node.next = current_node.next  # Link new node
            current_node.next = new_node  # Update links
            self.length += 1

    def delete_by_value(self, data):
        if self.head == None:
            print("Linked List is empty. Nothing to delete.")
            return
        current_node = self.head
        if current_node.data == data:
            self.head = self.head.next  # Update head
            if self.head == None or self.head.next == None:
                self.tail = self.head  # Update tail
            self.length -= 1
            return
        while current_node.next != None and current_node.next.data != data:
            current_node = current_node.next  # Traverse list
        if current_node.next != None:
            current_node.next = current_node.next.next  # Delete node
            if current_node.next == None:
                self.tail = current_node  # Update tail
            self.length -= 1
            return
        else:
            print("Given value not found.")


if __name__ == '__main__':
    l=LinkedList()
    l.append(1)
    l.append(2)
    l.append(3)
    l.prepend(0)
    l.prepend(-1)
    l.insert(2,100)
    l.delete_by_value(1)
    l.print_list()

    