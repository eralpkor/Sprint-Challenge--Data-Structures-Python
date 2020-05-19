

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if insert (incoming) value is less then current node value
        if value < self.value:
            # and if is not
            if not self.left:
                # set the value here
                self.left = BinarySearchTree(value)
            else:
                # keep searching
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        # check if target is greater then the Node value
        elif target > self.value:
            # go right if right is a BSTNode
            return self.right.contains(target) if self.right else False
        else:
            # go left if left is a BST
            return self.left.contains(target) if self.left else False

    # Return the maximum value found in the tree

    def get_max(self):
        current = self
        # Find the rightmost leaf node
        # As long as self.right exist keep going right;
        while current.right:
            # keep assigning right leaf to self (current)
            current = current.right
        # if no value left to the right return value
        return current.value


    def iterative_get_max(self):
        current_nax = self.value
        current = self
        # traverse our structure
        while current:
            if current.value > current_nax:
                current_nax = current.value
            # update our current max variable if we see a larger value
            current = current_nax
        return current_nax

    # Call the function `fn` on the value of each node

    def for_each(self, fn):
        # at the leaf node
        fn(self.value)
        # if left leaf exist
        if self.left:
            # call recursive
            self.left.for_each(fn)
        # if right leaf
        if self.right:
            # call recursive
            self.right.for_each(fn)

    # iterative for each depth first
    def iterative_for_each(self, fn):
        stack = []
        # add the root node
        stack.append(self)

        #loop so long as the stack still has elements
        while len(stack) > 0:
            current = stack.pop()
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

            fn(current.value)

    # # breadth first for each
    def breadth_first_for_each(self, fn):
        queue = deque()
        # add the root node
        queue.append(self)

        #loop so long as the stack still has elements
        while len(queue) > 0:
            current = queue.pop()
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            
            fn(current.value)

    # Part 2 -----------------------

#     # Print all the values in order from low to high
#     # Hint:  Use a recursive, depth first traversal
# # traversals require O(n) time as they visit every node exactly once.
    def in_order_print(self, node):
        if node.left:
            node.in_order_print(node.left)
        print(node.value)
        if node.right:
            node.in_order_print(node.right)

#     # Print the value of every node, starting with the given node,
#     # in an iterative breadth first traversal

#     def bft_print(self, node):
#         # print current node first then
#         # print to the right (largest node) until none
#         # go to left node (subtree) print first node
#         # print right subtree leafs left node
#         to_print = Queue()
#         to_print.enqueue(node)
#         current_node = to_print.dequeue()
#         while current_node: # is not None
#             # print current node 
#             print(current_node.value)
#             # if there is right node of current node, 
#             if current_node.right:
#                 # call Queue.enqueue until no right leaf (node)
#                 to_print.enqueue(current_node.right)
#             # if there is left node of current node

#             if current_node.left:
#                 to_print.enqueue(current_node.left)
#             if to_print.size > 0:
#                 current_node = to_print.dequeue()
#             else:
#                 # quit when Queue size is 0
#                 break

#     # Print the value of every node, starting with the given node,
#     # in an iterative depth first traversal
#     # Go left (small values) first then right (small leafs)
#     def dft_print(self, node):
#         to_print = Stack() # using stack
#         to_print.push(node) # add first node to the stack
#         # while stack length greater then 0
#         while to_print.__len__() > 0:
#             # pop the node from stack assign to var current
#             current = to_print.pop()
#             # print the current node value
#             print(current.value)
#             # if right node value exist 
#             if current.right:
#                 # add to tail
#                 to_print.push(current.right)
#             if current.left:
#                 to_print.push(current.left)

#     # Stretch Goals -------------------------
#     # Note: Research may be required

#     # Print Pre-order recursive DFT
#     def pre_order_dft(self, node):
#         pass

#     # Print Post-order recursive DFT
#     def post_order_dft(self, node):
#         pass


