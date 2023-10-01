
'''

return true if n is a power of 3, else return false
n == 3^x 
example: 
    n = 27
    27 / 3 -> 9
    9 / 3 -> 3
    3 / 3 -> 1

    base case:  x = 1, return true
                x%3 != 0, return false

    n = 28
    28 / 3 -> 9.3333
    9.3333 / 3 -> 3.3333
    3.33333 / 3 -> 1.333333
                           
🔎 EXPLORE
What are some other insightful & revealing test cases?
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
Write your algorithm.
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

def isPowerOfThree( n: int) -> bool:

    if n == 1:
        return True
    elif n <= 1: 
        return False
    return isPowerOfThree(n/3)
    # 27 / 3 -> 9
    # 9 / 3 ->  3
    # 3 / 3 ->  1