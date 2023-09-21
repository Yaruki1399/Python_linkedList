class DoublyLinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.prev = None
            self.next = None

    def __init__(self):
        self.head = None

    def insertFront(self, data):
        new_node = self.Node(data)

        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node

        self.head = new_node

    def insertNodeAfter(self, prev_node, data):
        if prev_node is None:
            print("Previous node can't be NONE!")
            return

        new_node = self.Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node

        if new_node.next is not None:
            new_node.next.prev = new_node

    def insertEnd(self, data):
        new_node = self.Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def deleteNode(self, del_node):
        if self.head is None or del_node is None:
            return

        if self.head == del_node:
            self.head = del_node.next
            if self.head is not None:
                self.head.prev = None

        if del_node.next is not None:
            del_node.next.prev = del_node.prev

        if del_node.prev is not None:
            del_node.prev.next = del_node.next

    def printlist(self):
        node = self.head
        while node is not None:
            print(f"{node.data}", end=" -> ")
            node = node.next
        print("\n")

double_linked_list = DoublyLinkedList()

double_linked_list.insertEnd(5)
double_linked_list.insertEnd(1)
double_linked_list.insertEnd(6)
double_linked_list.insertEnd(9)

node_to_insert_after = double_linked_list.head.next 
double_linked_list.insertNodeAfter(node_to_insert_after, 11)

node_to_insert_after = double_linked_list.head.next.next  
double_linked_list.insertNodeAfter(node_to_insert_after, 15)


print("The Double Linked List: ")
double_linked_list.printlist()

for _ in range(5):
    data = int(input("\nEnter data [a number] for a new node:  "))
    double_linked_list.insertEnd(data)

print("\n\nThe Updated Double Linked List: ")
double_linked_list.printlist() 
