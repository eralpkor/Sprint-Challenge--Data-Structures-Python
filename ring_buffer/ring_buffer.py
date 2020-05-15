from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        else:
            self.current.value = item
            self.current = self.current.next or self.storage.head

    def get(self):
        buffer_content = []

        current_node = self.storage.head
        while current_node:
            buffer_content.append(current_node.value)
            current_node = current_node.next

        return buffer_content




# is this a stretch
class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None] * capacity

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        elif len(self.storage) == self.capacity:
            self.storage[self.current] = item
            self.current = 0 if self.current == self.capacity - 1\
                            else self.current + 1

# https://stackoverflow.com/questions/311775/python-create-a-list-with-initial-capacity
    def get(self):
        return list(filter(None, self.storage))



# capacity = 5
# buffer = RingBuffer(capacity)

# buffer.append('a')
# buffer.append('b')
# buffer.append('c')
# buffer.append('d')
# buffer.append('e')
# buffer.append('f')
# buffer.append('g')
# buffer.append('h')
# buffer.append('i')

# printMe = buffer.get(), ['f', 'g', 'h', 'i', 'e']

# print(printMe)