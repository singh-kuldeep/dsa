class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, val):
        new_node = Node(val)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        print("self.length: ", self.length)
        # print("self.head: ", self.head)
        # print("self.tail: ", self.tail)
        head = self.head
        while head is not None:
            print(head.value)
            head = head.next

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        if self.head is None:
            self.head = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        elif self.head == self.tail:
            temp = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return temp.value
        else:
            pre = self.head
            temp = self.head
            while temp.next:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.length -= 1
            return temp.value

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length +=1
        return True

my_linked_list = LinkedList(3)
my_linked_list.append(4)


print(my_linked_list.pop())
print(my_linked_list.pop())
my_linked_list.prepend(2)
my_linked_list.prepend(1)
# print(my_linked_list.pop())

my_linked_list.print_list()
