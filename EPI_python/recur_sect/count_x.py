

'''
❓ PROMPT
Given a string, compute recursively (no loops) the number of lowercase 'x' chars in the string.

Example(s)
countX("xxhixx") == 4
countX("xhixhix") == 3
countX("hi") == 0
 

🔎 EXPLORE
List your assumptions & discoveries:
- empty string returns 0


Insightful & revealing test cases:
- splicing the string at each recursive step, check if string[0] is x or not

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O(N)
Space: O(N)
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function countX(word) {
def countX(word: str) -> int:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

def countX(word: str) -> int:

    if len(word) == 0:
        return 0
    
    if word[0] == 'x':
        return 1 + countX(word[1:])
    
    return countX(word[1:])

    
print(countX("xxhixx") == 4)
print(countX("xhixhix") == 3)
print(countX("hiX") == 0)
print(countX("XXXhXXX") == 0)
print(countX("x") == 1)
print(countX("") == 0)
print(countX("hihi") == 0)
print(countX("hiAAhi12hi") == 0)