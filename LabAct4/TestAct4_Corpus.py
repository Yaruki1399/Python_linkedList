class CreateList:
    # Represents the node of the list.
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        # Declaring head and tail pointer as None.
        self.head = None
        self.tail = None

    # This function will add the new node at the end of the list.
    def add(self, data):
        # Create a new node
        new_node = self.Node(data)
        # Checks if the list is empty.
        if self.head is None:
            # If the list is empty, both head and tail would point to the new node.
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            # Tail will point to the new node.
            self.tail.next = new_node
            # New node will become the new tail.
            self.tail = new_node
            # Since it is a circular linked list, tail will point to head.
            self.tail.next = self.head

    # Displays all the nodes in the list.
    def display(self):
        current = self.head
        if self.head is None:
            print("List is empty")
        else:
            print("\nNodes of the circular linked list:")
            while True:
                # Prints each node by incrementing pointer.
                print(f"\n  {str(current.data)}", end='')
                current = current.next
                if current == self.head:
                    break
            print()

if __name__ == "__main__":
    cl = CreateList()
    
    # Ask for data from users using a loop
    for i in range(5):
        data = int(input(f"Enter data for node {i+1}:  "))
        cl.add(data)

    # Displays all the nodes present in the list
    cl.display()
