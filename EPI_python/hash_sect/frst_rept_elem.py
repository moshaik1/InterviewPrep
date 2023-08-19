

'''
❓ PROMPT
Given an array, return the first element is repeated if you were to traverse the array from left to right.

Example(s)
firstRepeatedElement([1, 2, 3, 2, 1, 1]) == 2
 

🔎 EXPLORE
List your assumptions & discoveries:
 
-empty? -> -1
- if only 1 element in array -> -1
- what if no elements repeat? -> -1


Insightful & revealing test cases:

print(firstRepeatedElement([]))
print(firstRepeatedElement([ 4 ]))
print(firstRepeatedElement([ 1 , 2 , 3 , 4 , 5]))
print(firstRepeatedElement([ 1 , 2 , 3 , 4 , 1 , 2]))
print(firstRepeatedElement([ 1 , 2 , 3 , 4 , 1 , 2 , 1]))
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1: have an empty set. traverse throught the array left to right, check if current element is in the set, if not add to set. But if in set, return element at first repeat
Time: O(n)
Space: O(n)
 

📆 PLAN
Outline of algorithm #: 

 

🛠️ IMPLEMENT
function firstRepeatedElement(arr) {
def firstRepeatedElement(arr: list[int]) -> int: 
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

def firstRepeatedElement(arr: list[int]) -> int:
    testSet = set()

    if not arr or len(arr) == 1:
        return -1
    
    for i in range(0, len(arr)):
        if arr[i] not in testSet:
            testSet.add(arr[i])
        else:
            return arr[i]
        
    
    return -1


print(firstRepeatedElement([])) # -1
print(firstRepeatedElement([ 4 ])) # -1
print(firstRepeatedElement([ 1 , 2 , 3 , 4 , 5])) # -1
print(firstRepeatedElement([ 1 , 2 , 3 , 4 , 1 , 2])) # 1
print(firstRepeatedElement([ 1 , 2 , 3 , 4 , 2 , 2 , 1])) # 2
 