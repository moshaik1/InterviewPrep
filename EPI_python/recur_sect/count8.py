

'''
❓ PROMPT
Given a non-negative int n, compute recursively (no loops) the number of occurrences of 8 as a digit,
except that an 8 with another 8 immediately to its left counts double, so 8818 yields 4 (because 1+2+0+1).

Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while dividing (/) by 10 removes the rightmost digit (126 / 10 is 12).

Example(s)
count8(8) == 1
count8(818) == 2
count8(8818) == 4  (because 1+2+0+1)
 

🔎 EXPLORE
List your assumptions & discoveries:
- non negative
- base case: if n <= 0: return 0
 

Insightful & revealing test cases:



🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function count8(n) {
def count8(n: int) -> int:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''


def count8(n: int) -> int:
    if n <= 0:
        return 0
    
    

    # used to check for consecutive 8's
    if n % 10 == 8:
            return 1 + count8(n // 10)
    if n % 100 == 88:
            return 2 + count8(n // 10)

    
    return count8(n // 10)