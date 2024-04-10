class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next = next_node
        self.prev = prev_node

    def set_value(self, value):
        self.value = value

    def set_next_node(self, next_node):
        self.next = next_node

    def set_prev_node(self, prev_node):
        self.prev = prev_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next

    def get_prev_node(self):
        return self.prev


class LinkedImage:
    def __init__(self, width=None, height=None):
        self.head = None
        self.tail = None
        self.width = width
        self.height = height
        self.length = 0

    # returns n in LinkedImage and iterates tail to head
    def __iter__(self):
        n = self.tail
        while n:
            yield n
            n = n.prev

    # returns n in LinkedImage and iterates head to tail
    def get_all_nodes(self):
        n = self.head
        while n:
            yield n
            n = n.next

    def get_head_node(self):
        return self.head

    def insert_beginning(self, value):
        new_head = Node(value)
        current_head = self.head

        if current_head != None:
            current_head.set_prev_node(new_head)
            new_head.set_next_node(current_head)

        self.head = new_head
        self.length += 1

        if self.tail == None:
            self.tail = new_head

    def stringify_list(self):
        string_list = ""
        current_node = self.head
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string_list


# code to test:
"""
colour_matrix = LinkedImage(width, height)
for n in colour_matrix:
    print(n.value)
"""
