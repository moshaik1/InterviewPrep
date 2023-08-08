
# ARRAYS
#  - list type that is mutable and is dynamically resizable, no bounds on how many values can be added, inserted, or removed from the list

#  TIPS FOR EFFICIENCY: 
# - see if it's possible to write values to back instead of front, it's faster
# - instead of deleting values, type to overwrite them, it's faster
# - be comfortable with subarrays


# INSTANTIATING AN ARRAY 
# - [1 , 2  , 3]
# - [1] + [2] * 10 
# - list(range(10)) 

# BASIC OPERATIONS
# - len , .append(), .remove(), .insert( , )

# 2-D arrays  instantiate
# [[1 , 2 , 3], [ 5 , 8 , 9 , 10]]
# [[1] * 4 for i in range(4)]
# 


# check if value is present in array
# - "in A"

# How do copies work? 
#  A REFERENCE, NOT A COPY  
#   B = A 
#  SHALLOW COPY 
#      - using B = list(A)
#      - using B = A[:]
#      - using copy library
#         - B  = A.copy()

#  DEEP COPY
#     - using deepcopy from copy library
#        - B = A.deepcopy()
#
#  IMPORTANT OPERATIONS
#     - len() , .append(), .remove(), .insert() 
#
#
#
#  KEY METHODS AND STATEMENTS
#     - min() 
#     - max()
#     - binary search for ordered list
#     - .reverse() , reversed(A)
#     - .sort() , sorted(A)
#     - del A[3] , del A[i:j]


# LIST COMPREHENSION
# [x**2 for x in range(6)] => [0 , 1 , 4 , 9 , 16 , 25]
# [x**2 for x in range(6) if  x % 2 == 0] => [0 , 4 , 16]
# 
# SUPPORTS MULTIPLE LEVELS OF LOOPING
#    - A = [ 1 , 2 , 3 ]    B = [ 4 , 5 , 6]
#    - [(x,y) for x in A for y in B]