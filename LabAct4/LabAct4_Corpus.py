class CreatedLists:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
            self.head = None
            self.tail = None

    def add(self,data):
        new_node = self.Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head

    def display(self):
        current = self.head
        if self.head is None:
            print("List is empty")
        else:
            print("\nNodes of the circular linked list:")
            while True:
                print(f" {str(current.data)} ->", end='')
                current = current.next
                if current == self.head:
                    break
            print()


if __name__ == "__main__":
    cl = CreatedLists()

    for i in range(5):
        data = int(input(f"\nEnter the data for node {i + 1}: "))
        cl.add(data)

    cl.display()