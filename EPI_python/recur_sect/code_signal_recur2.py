"""
Given a string with nested parentheses, return the substring between the parentheses at the specified depth.

Input: "ab(c(def)gh)i", depth=1
Output: "c(def)gh"
Input: "ab(c(def)gh)i", depth=2
Output: "def"
The string is guaranteed to have balanced parentheses, i.e. every ( character has a corresponding ) character, and every level has at most 1 parenthesis nesting, i.e. (()()) will not occur.

If the depth is greater than the maximum parentheses depth in the string, return an empty string.

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string parenString

The string containing balanced parentheses

Constraints: balanced parentheses and at most 1 nesting of parentheses per level

[input] integer depth

The nesting level to navigate inward to

Constraints: 0 <= depth <= 10000

[output] string

The substring between two parentheses

"""
def solution(parenString, depth):

    if depth == 0:
        print(parenString)
        return parenString
        
    if len(parenString) == 0 :
        return ""
    
        
    # left side
    if parenString[0] != '(':
        print(parenString)
        return solution(str(parenString[1:]), depth)
    
    # right side
    if parenString[-1] != ')':
        print(parenString)
        return solution(str(parenString[ : -1]), depth)
    
    if parenString[0] == '(' and parenString[-1] == ')':
        print(parenString)
        return solution(str(parenString[1:-1]), depth - 1)
        
"""
Given an integer index n, find the nth Fibonacci number.

Note: Write a solution with O(n) complexity and O(1) additional memory.

Example

For n = 2, the output should be
solution(n) = 1.

F2 = F0 + F1 = 0 + 1 = 1

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] integer n

Guaranteed constraints:
1 ≤ n ≤ 15.

[output] integer
"""

def solution(n):
    
    if n == 0 or n == 1:
        return n
        
    return solution(n-1) + solution(n-2)
    
