

'''
❓ PROMPT
Let's practice recursion by converting functions to and from recursive implementations. Copy the started code in the language of your choice below, then implement the missing functions and test! 

While reading the recursive implementation of *recursiveFactorial* as well as writing *recursiveMax*, consider the following:

1. What is my base case?
2. Which arguments do I need?
3. What do I do at each recursive step?

Example(s)
iterativeFactorial(3) -> 6
iterativeFactorial(4) -> 24

recursiveMax([4, 2, 7] -> 7
recursiveMax([1, -5, 0] -> 1
 

🔎 EXPLORE
List your assumptions & discoveries:
1. recurFactorial:
    - 3! -> 3 * 2! -> 3 * 2 * 1

- base case: if x = 1, return 1
- non negative and non zero?


Insightful & revealing test cases:
 - input: 1
 - input: 2
 - input: 3

🧠 BRAINSTORM
What approaches could work?
Algorithm 1: breaking factor of n down to -> n * (n-1)! until n = 1 
Time: O() 
Space: O()
 

📆 PLAN
Outline of algorithm #: 

4! ->     4 * 3! ->     4 * 3 * 2! ->      4 * 3 * 2 * 1!   
x = 4     x = 3         x = 2              x = 1 
 
base case: if x <= 1, return 1
🛠️ IMPLEMENT

Python Starter Code

def recursiveFactorial(x: int) -> int:
  if x <= 1:
    return 1
  return x * recursiveFactorial(x - 1)

def iterativeFactorial(x: int) -> int:
  
    

  
------------------------------------------------------------------------
def iterativeMax(arr):
  result = arr[0] if len(arr) > 0 else None

  for i in range(1, len(arr)):
    if arr[i] > result:
      result = arr[i]

  return result

def recursiveMax(arr: list[int], curMax=float('-inf'), i = 0) -> int:
  # curMax is an argument that defaults to null if not specified when calling recursiveMax()
  # i is an argument that defaults to 0 if not specified when calling recursiveMax()
  # return null if array is empty
  pass # TODO: implement
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
# 4!

# def recursiveFactorial(x: int) -> int:
#   if x <= 1:
#     return 1
#   return x * recursiveFactorial(x - 1)

# def iterativeFactorial(x: int) -> int:
#     temp = x
#     accum = 1
#     while temp >= 1:
#         accum = accum * temp
#         temp -= 1
#     return accum

# print(recursiveFactorial(4))
# print(iterativeFactorial(4))   


def iterativeMax(arr):
  result = arr[0] if len(arr) > 0 else None

  for i in range(1, len(arr)):
    if arr[i] > result:
      result = arr[i]

  return result

def recursiveMax(arr: list[int], curMax=float('-inf'), i = 0) -> int:
  # curMax is an argument that defaults to null if not specified when calling recursiveMax()
  # i is an argument that defaults to 0 if not specified when calling recursiveMax()
  # return null if array is empty

    if i < len(arr):
       return recursiveMax(arr, max(curMax, arr[i]), i + 1)
    return curMax
       
print(recursiveMax([3 , 5, 1]))
    


  
 
