import time
from binary_search_tree_short import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# # Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

'''The above code runs in O(n^2) time.
For any inputs, the code must calculate
the cartesian product of the two lists.
In the worst-case scenario, the lists
are of equal length.

My answer (below) runs in O(n log(n)) time
using a binary search tree.'''

tree_1 = BinarySearchTree(None)

for name_1 in names_1:
    tree_1.insert(name_1)

duplicates = [name_2 for name_2 in names_2 if tree_1.contains(name_2)]

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# This runs in 0.0029 seconds on my machine.
duplicates = list(set(names_1).intersection(names_2))
