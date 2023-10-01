

'''
❓ PROMPT
Given a string and a non-empty substring *sub*, compute recursively the number of times that sub appears in the string, without the substrings overlapping.

Example(s)
strCount("catcowcat", "cat") == 2
strCount("catcowcat", "cow") == 1
strCount("catcowcat", "dog") == 0
 

🔎 EXPLORE
List your assumptions & discoveries:
- no overlaps!! so need to slice properly
- if sub >= string, return False
- if n == 0  return True -> base case
 

Insightful & revealing test cases:
strCount("wowowtop", "wow") == 1     #overlapping
strCount("catcowcat", "cat") == 2    #normal case even 
strCount("catcowcatcowcat", "cat") == 3  #normal case odd
strCount("clow", "clown") == 0    # sub > str
strCount("", "cat") == 0   # empty string
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O(N)
Space: O(N)
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function strCount(word,  sub) {
def strCount(word: str,  sub: str) -> int:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

def strCount(word: str,  sub: str) -> int:

    subLeng = len(sub)

    if len(sub) > len(word):
        return 0

    
    if word[0: subLeng] == sub:
        return 1 + strCount(word[subLeng:], sub)
    
    return strCount(word[1:], sub)


print(strCount("catcowcat", "cat") == 2)
print(strCount("catcowcat", "cow") == 1)
print(strCount("catcowcat", "dog") == 0)
print(strCount("cacatcowcat", "cat") == 2)
print(strCount("xyx", "x") == 2)
print(strCount("iiiijj", "i") == 4)
print(strCount("iiiijj", "ii") == 2)
print(strCount("iiiijj", "iii") == 1)
print(strCount("iiiijj", "j") == 2)
print(strCount("iiiijj", "jj") == 1)
print(strCount("aaabababab", "ab") == 4)
print(strCount("aaabababab", "aa") == 1)
print(strCount("aaabababab", "a") == 6)
print(strCount("aaabababab", "b") == 4)