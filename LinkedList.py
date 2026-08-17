class Node:
    """Node class for LinkedList"""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """LinkedList implementation with common operations"""
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """Insert a node at the beginning of the list"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Insert a node at the end of the list"""
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_position(self, data, position):
        """Insert a node at a specific position (0-indexed)"""
        if position < 0:
            print("Position cannot be negative")
            return
        
        new_node = Node(data)
        
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        prev = None
        count = 0
        
        while current and count < position:
            prev = current
            current = current.next
            count += 1
        
        if count == position:
            new_node.next = current
            prev.next = new_node
        else:
            print("Position out of range")

    def delete_at_beginning(self):
        """Delete the first node"""
        if not self.head:
            print("List is empty")
            return
        self.head = self.head.next

    def delete_at_end(self):
        """Delete the last node"""
        if not self.head:
            print("List is empty")
            return
        
        if not self.head.next:
            self.head = None
            return
        
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def delete_at_position(self, position):
        """Delete a node at a specific position (0-indexed)"""
        if position < 0:
            print("Position cannot be negative")
            return
        
        if not self.head:
            print("List is empty")
            return
        
        if position == 0:
            self.head = self.head.next
            return
        
        current = self.head
        prev = None
        count = 0
        
        while current and count < position:
            prev = current
            current = current.next
            count += 1
        
        if current:
            prev.next = current.next
        else:
            print("Position out of range")

    def search(self, data):
        """Search for a node with specific data"""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def display(self):
        """Display all elements in the list"""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) if elements else "Empty List")

    def get_length(self):
        """Return the length of the list"""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def reverse(self):
        """Reverse the linked list"""
        prev = None
        current = self.head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev

    def is_empty(self):
        """Check if the list is empty"""
        return self.head is None


# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    
    # Insert elements
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    ll.insert_at_end(40)
    
    print("LinkedList after insertions:")
    ll.display()
    
    # Insert at beginning
    ll.insert_at_beginning(5)
    print("\nAfter inserting 5 at beginning:")
    ll.display()
    
    # Insert at position
    ll.insert_at_position(15, 2)
    print("\nAfter inserting 15 at position 2:")
    ll.display()
    
    # Search
    print(f"\nSearch for 20: {ll.search(20)}")
    print(f"Search for 100: {ll.search(100)}")
    
    # Length
    print(f"\nLength of LinkedList: {ll.get_length()}")
    
    # Delete at end
    ll.delete_at_end()
    print("\nAfter deleting last node:")
    ll.display()
    
    # Delete at beginning
    ll.delete_at_beginning()
    print("\nAfter deleting first node:")
    ll.display()
    
    # Reverse
    ll.reverse()
    print("\nAfter reversing:")
    ll.display()
