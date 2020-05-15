import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# RUNTIME ANALYSIS:
# This nested loops takes around 10 seconds on my PC.
# The runtime complexity of the nested loop would be O(m * n) where m is the number of 
# elements in the first list (names_1) and n is the number of elements in the second 
# list (names_2). If we know that the two lists would always have the same number of 
# elements n, then O(m * n) becomes O(n^2), or quadratic time.


# BStree = BinarySearchTree('eralp')

# for name_1 in names_1:
#     BStree.insert(name_1)

# for name_2 in names_2:
#     if BStree.contains(name_2):
#         duplicates.append(name_2)

# RUNTIME ANALYSIS:
# The original code takes around 10 seconds to run on my computer. Code utilizing a
#  Binary Search Tree (BST) takes around 0.18 seconds to run on my computer.
# The runtime complexity of the code utilizing BST is O(n log n), linearithmic time,
#  since it loops through each element in the names_2 list once, but it utilizes binary
#  search to eliminate half of the remaining elements with each pass.




# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  There are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# RUNTIME ANALYSIS:
# runtime: 0.007998228073120117 seconds :zap:

# Code using Python's built-in set data structure and its intersection method takes less
#  than one-hundredth of a second to run on my computer.
# The runtime complexity using sets is O(m + n), where m is the number of elements in 
# the first list (names_1) and n is the number of elements in the second list (names_2).
#  This would result in linear time complexity.

duplicates = list(set(names_1).intersection(names_2))

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")


