class node:
    def __init__(self, data=None):
        self.data=data
        self.next=None #used as a storage for the pointer of the next node
        # The last pointer element in a linked list is ALWAYS set to none

    # LINKED LIST CLASS - acts as a wrapper for the nodes above ^^ {def __init__(self, data=None):} which is a sub-class of a linked list

class linked_list:
    def __init__(self):
        self.head = node() # << HEAD NODE - not indexable and no accessible data; only works as a PLACEHOLDER


    # append function which adds the new datapoint to the END of the current list (creates the first element of tyhe list)

    def append(self,data):
        new_node = node(data)
        curr = node(data)
        # the while condition will continue iterating until the data value will be NULL or None
        while curr.next!=None:
            curr = curr.next #continues to traverse through the list
        curr.next = new_node # << last element of the list - set the LAST node as the NEW node


    # lenghth(self) function will calculate the length of the list
    
    def length(self):
        curr = self.head   #variable that points to the current node
        total = 0
        while curr.next!=None:
            total+=1 # increments the total value
            curr = curr.next # increments to the next node
        return total #returns the total value for STORAGE
    
    def display(self):
        elems = [] # storage for a list of elements
        curr_node = self.head
        while curr_node!=None:
            curr_node = curr_node.next
            elems.append(curr_node.data)
        print elems

my_list = linked_list()

my_list.display()