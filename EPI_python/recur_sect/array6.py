
'''
❓ PROMPT
Given an array of ints, compute recursively the number of times that the value 6 appears in the array. 
We'll use the convention of considering only the part of the array that begins at the given index. 
In this way, a recursive call can pass index+1 to move down the array. The initial call will pass in index as 0.

Example(s)
array6([1, 2, 6], 0) == 1
array6([6, 6], 0) == 2
array6([1, 2, 3, 4], 0) == 0
 

🔎 EXPLORE
List your assumptions & discoveries:
- if array if shorter than index stated, return 0


Insightful & revealing test cases:
- index longer than array length
- 6 before index 
- 6 after index
- multiple 6s in array
- no 6s in array

🧠 BRAINSTORM
What approaches could work?
Algorithm 1: iterating through array, starting at index until array is empty
Time: O(N)
Space: O(N)
 

📆 PLAN
Outline of algorithm #: 
- base case: getting to end of array, return 0
- check if index is longer than array length
- starting at index, recur call until base case is reached, adding 1 if char is '6

🛠️ IMPLEMENT
function array6(nums, index) {
def array6(nums: list[int], index: int) -> int:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
# [0,4,6,9,6] , 2

def array6(nums: list[int], i: int) -> int:

    if i >= len(nums): 
        return 0
    
    if nums[i] == 6:
        return 1 + array6(nums, i+1)
    
    return array6(nums, i+1)

print(array6([1, 2, 6], 0) == 1)
print(array6([6, 6], 0) == 2)
print(array6([1, 2, 3, 4], 0) == 0)
print(array6([1, 6, 3, 6, 6], 0) == 3)
print(array6([6], 0) == 1)
print(array6([1], 0) == 0)
print(array6([], 0) == 0)
print(array6([6, 2, 3, 4, 6, 5], 0) == 2)
print(array6([6, 5, 6], 0) == 2)