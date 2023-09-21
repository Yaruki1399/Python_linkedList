class DoublyLinkedList:
    class Node:
        def __init__(self, data):
            self.data = data  # Initialize the node's data
            self.prev = None  # Initialize the previous node reference
            self.next = None  # Initialize the next node reference

    def __init__(self):
        self.head = None  # Initialize the head of the doubly linked list

    def insertFront(self, data):
        """
        Insert a node with the given data at the front of the linked list.
        """
        new_node = self.Node(data)  # Create a new node with the provided data
        new_node.next = self.head  # Set the next reference of the new node to the current head

        if self.head is not None:
            self.head.prev = new_node  # If the list is not empty, update the previous reference of the current head

        self.head = new_node  # Update the head to the new node

    def insertAfter(self, prev_node, data):
        """
        Insert a node with the given data after a specified previous node.
        """
        if prev_node is None:
            print("Previous node cannot be None")
            return

        new_node = self.Node(data)  # Create a new node with the provided data
        new_node.next = prev_node.next  # Set the next reference of the new node
        prev_node.next = new_node  # Update the next reference of the previous node
        new_node.prev = prev_node  # Update the previous reference of the new node

        if new_node.next is not None:
            new_node.next.prev = new_node  # Update the previous reference of the node after the new node

    def insertEnd(self, data):
        """
        Insert a node with the given data at the end of the linked list.
        """
        new_node = self.Node(data)  # Create a new node with the provided data
        temp = self.head  # Temporary reference to traverse the list

        new_node.next = None  # Set the next reference of the new node

        if self.head is None:
            new_node.prev = None  # If the list is empty, set the previous reference of the new node
            self.head = new_node  # Update the head to the new node
            return

        while temp.next is not None:
            temp = temp.next  # Traverse to the end of the linked list

        temp.next = new_node  # Update the next reference of the last node
        new_node.prev = temp  # Update the previous reference of the new node

    def deleteNode(self, del_node):
        """
        Delete a specified node from the doubly linked list.
        """
        if self.head is None or del_node is None:
            return

        if self.head == del_node:
            self.head = del_node.next  # If the head node is the node to delete, update the head

            if self.head is not None:
                self.head.prev = None  # Update the previous reference of the new head

        if del_node.next is not None:
            del_node.next.prev = del_node.prev  # Update the previous reference of the node after the deleted node

        if del_node.prev is not None:
            del_node.prev.next = del_node.next  # Update the next reference of the previous node

    def printlist(self):
        """
        Print the elements of the doubly linked list.
        """
        node = self.head
        while node is not None:
            print(node.data, end=" -> ")  # Print the data of the current node
            node = node.next
        print()  # Print a newline to separate the output

# Create a new doubly linked list
doubly_ll = DoublyLinkedList()

# Insert initial nodes (as shown in the example)
doubly_ll.insertEnd(5)
doubly_ll.insertFront(1)
doubly_ll.insertFront(6)
doubly_ll.insertEnd(9)
doubly_ll.insertAfter(doubly_ll.head, 11)
doubly_ll.insertAfter(doubly_ll.head.next, 15)

# Print the current list
print("Doubly Linked List:")
doubly_ll.printlist()

# Add 5 more nodes based on user input
for _ in range(5):
    data = int(input("Enter data for a new node: "))
    doubly_ll.insertEnd(data)

# Print the updated list
print("Updated Doubly Linked List:")
doubly_ll.printlist()
