
"""

Hashmaps:

-   keys are immutable and must be unique
-   similiar to arrays but uses keys instead of numeric indexing

- adding element, searching for element, removing element = 0(1) , unlike arrays: 0(n) or 0(logN)

    - the reason it is 0(n) to Hash is beacuse getting the key's index value is independent of the number of keys in the collection
- iterating is still 0(n)
- Hash functions are imperfect, can sometimes result in collisions but they are resolved internally

- very useful if youre querying/searching alot 


Hashmap Explaination:

Key -> Hashing function -> Value

- the Hashing function maps keys to numeric indices, and the indices map to Values


Hashsets:

Key -> Hashing function
- cannot access using index 
- unordered collection of unique keys, can be any data type
- adding, searching, and removing specific keys -> O(1)
- can check and see if key is a member of a set or not
- can iterate over set


- Very Useful For:
    - checking for existance of an element
    - finding duplicates
    - finding overlapping elements betweeen 2 collections
    - finding the difference between 2 collections
    - can help algorithms remember what they have already encountered

Questions to ask yourself:
    - what do keys represent
    - Will my algorithm know the key to search for in the set?
    - How will using the uniqueness constraint help?
    - Will the unordered nature impact you?

"""

numbers = [1 , 1 , 2 ,3 ,4 ,5]
first = set(numbers)
print(print)

second = {1 ,3 ,6 , 7 , 4}
print(second)

second.add(5)
second.remove(4)
len(second)

#UNION (ALL ITMES IN FIRST AND SECOND)

unionEx = first | second
print(unionEx)

#INTERSECTION (COMMON IN BOTH FIRST AND SECOND)
interEx = first & second
print(interEx)

#DIFFERENCE (WHATS IN FIRST BUT NOT SECOND)
diffEx = first - second
print(diffEx)

#SYMETRIC DIFFERENCE (WHATS IN FIRST AND SECOND BUT NOT BOTH)
sydiffEx = first ^ second
print(sydiffEx)