
'''
❓ PROMPT
In mathematics, the factorial of a non-negative integer N, denoted as N!, is the multiplication product of all positive integers <= N. Compute the result recursively (without loops).

Example(s)
factorial(3) == 6
factorial(5) == 120
 

🔎 EXPLORE
List your assumptions & discoveries:
- non negative and non zero

Insightful & revealing test cases:
- base case is if x = 1 return 1
- x >= 1

🧠 BRAINSTORM
What approaches could work? 
Algorithm 1:
Time: O(n) 
Space: O(n) -> n number of frames on the call stack
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function factorial(n) {
def factorial(n: int) -> int:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
def factorial(n: int) -> int:
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(12) == 479001600)
print(factorial(10) == 3628800)
print(factorial(5) == 120)
print(factorial(3) == 6)
print(factorial(2) == 2)
print(factorial(1) == 1)
