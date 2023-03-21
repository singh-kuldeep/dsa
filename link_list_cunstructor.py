class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        """ create a node """
        new_node = Node(value=value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        """ add an element in the end """
        new_node = Node(value=value)
        if self.head is None:
            """ head and tail point to None --> length 0 """
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

        return True

    def insert(self, index, value):
        """ insert an element at any location """
        pass

    def pop(self):
        """ remove an element from the end """
        if self.length == 0:
            return None

        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next

        self.tail = pre
        pre.next = None

        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value

    def prepend(self, value):
        """ add an element at the start """
        new_node = Node(value=value)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return True
        second = self.head.next
        self.head.next = None
        self.head = second
        return True

    def remove(self):
        """ remove an element from any location """
        pass


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.print_list()
my_linked_list.pop()
my_linked_list.prepend(3)
print("\nAfter")
my_linked_list.pop_first()
my_linked_list.print_list()
