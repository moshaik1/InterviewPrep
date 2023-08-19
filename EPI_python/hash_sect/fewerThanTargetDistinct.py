

'''
❓ PROMPT
Given an array and a target count X, return true if there are less than X distinct values in the array. For example, given [1, 2, 2, 3, 3] and 4, return true because there are only 3 distinct values 1, 2, and 3.

Example(s)
[1, 2, 2, 3, 3], 3 => false (there are exactly 3 distinct values)
[1, 2, 2, 3, 4], 3 => false (there are 4 distinct values)
[1, 1, 2, 2, 2], 3 => true (there are exactly 2 distinct values)
 

🔎 EXPLORE
List your assumptions & discoveries:

- empty array and target of 0?
- []
- distinct values >= target = False
- distinct values < target = True
 

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1: iterate through the array, have an empty set, if number is in set, counter += 1, else continue
Time: O(n)
Space: O(n)
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function fewerThanTargetDistinct(arr, target) {
def fewerThanTargetDistinct(arr: list[int], target: int) -> bool:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

def fewerThanTargetDistincy(arr: list[int], target:int) -> bool:

    counter = 0
    numSet = set()

    if not arr and target != 0:
        return False
    else:
        for num in arr:
            if num not in numSet:
                numSet.add(num)
                counter += 1
            
            if counter >= target:
                return False
    
    return True


print(fewerThanTargetDistincy([],0)) #True
print(fewerThanTargetDistincy([],1)) #False
print(fewerThanTargetDistincy([1 , 2 , 1],1)) # False
print(fewerThanTargetDistincy([1 , 2 , 3 , 1],4)) # True