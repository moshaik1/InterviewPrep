
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

- like a bucket, with a label (key) and a value

    - Very Useful For:
        - Counting the frequency of occurences
        - Grouping elements by a common property
        - Eliminating expensive lookups by remembering search results
        - Eliminating recalculations by caching results (memoization)
        - Correlating a unique trait with an unrelated attribute
    
    - Questions to ask yourself
        - Can you solve the problem more easily with a set?
        - What is the purpose of the value associated with each key?
        - What will the keys and values represent?
        - Will my algorithm know the key to search for in the map?
        - How will the uniqueness constraint help?
        - Will the unordered nature impact you?
    
    - Down side:
        - no guaranteed order, no indexing, no concept of first and last element

    - Should I use MapSet or HashMap
        - do I need a value to correspond to a key, is it necessary
"""

student = { 'name' : 'Mohsin' , 'age' : '24' , 'courses' : ['chemistry','bio'] }
print(student.get('name')) 

# .get() is very useful to check if key:value exists. If key doesnt exist, returns None. 2nd argument is default value

print(student.get('birthdate','Not Found'))

# adding to dictionary

student['friend'] = 'Siddhant'

# updating in dictionary

student['name'] = 'Jaspreet'
print(student)
student.update({'name': 'Mohsin' , 'friend': 'Nabeel'})
print(student)

# delete in dictionary

del student['age']

# delete in dictionary and return the value that was deleted

nameStud = student.pop('name')
print(nameStud)
student['name'] = 'Mohsin'
# see all keys

print(student.keys())

# see all values

print(student.values())

# see keys and values

print(student.items())

# iterating through

for key, val in student.items():
    print(key, val)

"""
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


print(" --------------------------")
numbers = [1 , 1 , 2 ,3 ,4 ,5]
first = set(numbers)
print(first)

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