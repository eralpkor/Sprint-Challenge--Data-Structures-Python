class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if node.get_next() is not None:

            next_node_to_make_head = node.get_next()
            self.reverse_list(next_node_to_make_head, None)

    # Tail recursion
    def reverseUtil(self, curr, prev):
        # If last node mark it head
        if curr.get_next() is None:
            self.head = curr

            # Update next to prev node
            curr.set_next(prev)
            return

        # Save curr.next node for recursive call
        next = curr.get_next()

        # And update next
        curr.set_next(prev)

        self.reverseUtil(next, curr)

    # This function mainly calls reverseUtil()
    # with previous as None
    def reverse_list(self, node, pre): 
        if self.head is None: 
            return 
        self.reverseUtil(self.head, None) 


# sll = LinkedList()

# sll.add_to_head(1)
# sll.add_to_head(2)
# sll.add_to_head(3)
# sll.add_to_head(4)
# sll.add_to_head(5)

# print('Before reverse')
# print(sll.head.value)
# print(sll.head.get_next().value)
# print(sll.head.get_next().get_next().value)
# print(sll.head.get_next().get_next().get_next().value)


# # after reverse
# sll.reverse(sll.head)
# print('After reverse')
# print(sll.head.value)
# print(sll.head.get_next().value)
# print(sll.head.get_next().get_next().value)
# print(sll.head.get_next().get_next().get_next().value)


# reverse.reverse_list()


