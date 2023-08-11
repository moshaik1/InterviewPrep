

'''
❓ PROMPT
Because strings are immutable, this problem takes more work than it does for an array. With an array, we can move individual values around and assign them into different locations. But with a string, we need to actually create an entirely new one.

Yes, in many modern languages this can be done with built in methods, but here we're working on basic coding patterns and coding fluency. We're going to mostly write this out.

Example(s)
reverseString("noitamroF") => "Formation"
 

🔎 EXPLORE
List your assumptions & discoveries:
 
- empty?
- should a new string be created?

Insightful & revealing test cases:
 
- ""
- "b"
- "ba"
- "cab"

🧠 BRAINSTORM
What approaches could work?
Algorithm 1: iterate the string backwards and add chars to new string
Time: O(n)
Space: O(n)
 

📆 PLAN
Outline of algorithm #: 
    -   have an empty string
    -   have a pointer that points to the last element of the input string
    -   loop through the string and move the pointer to the left for every iteration until it gets to the first element
    -   as you loop through the input string, populate the new string with the char that the pointer is pointing to
 

🛠️ IMPLEMENT
function reverseString(s)
def reverseString(s):
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

def reverseString(input:str)-> str:
    answer = ""
    for i in range(len(input)-1, -1 , -1):
        answer += input[i]
    
    return answer


print(reverseString(""))
print(reverseString("b"))
print(reverseString("bac"))
print(reverseString("llab"))

