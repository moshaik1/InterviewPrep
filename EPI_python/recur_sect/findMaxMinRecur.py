

'''
❓ PROMPT
Given an array, write 2 recursive functions to find the minimum and maximum element in an array.
You may use the *min(a,b)* and *max(a,b)* functions to shorthand picking the minimum and maximum between 2 values.

Example(s)
findMin([12, 1234, 45, 67, 1]) == 1
findMin([10, 20, 30]) == 10
findMin([8, 6, 7, 5, 3, 7]) == 3

findMax([12, 1234, 45, 67, 1]) == 1234
findMax([10, 20, 30]) == 30
findMax([8, 6, 7, 5, 3, 7]) == 8
 

🔎 EXPLORE
List your assumptions & discoveries:
- len(arr) == 0 -> return 0
- len(arr) == 1 -> return arr[0] -> Base case


Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1: 
Time: O()
Space: O()
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function findMin(arr) {
function findMax(arr) {
def findMin(arr: list[int]) -> int:
def findMax(arr: list[int]) -> int:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

def findMin(arr: list[int]) -> int:
    
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    
    
    return min(arr[0] , findMin(arr[1:]))

def findMax(arr: list[int]) -> int:
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    
    return max(arr[0] , findMax(arr[1:]))


print(findMin([12, 1234, 45, 67, 1]) == 1)
print(findMin([10, 20, 30]) == 10)
print(findMin([8, 6, 7, 5, 3, 7]) == 3)

print(findMax([12, 1234, 45, 67, 1]) == 1234)
print(findMax([10, 20, 30]) == 30)
print(findMax([8, 6, 7, 5, 3, 7]) == 8)