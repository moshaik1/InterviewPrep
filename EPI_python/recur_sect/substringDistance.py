

'''
❓ PROMPT
Given a string and a non-empty substring *sub*, compute recursively the 
size of the largest substring which starts and ends with the given *sub* string and return its length, 
including the length of the substrings. When *sub* is multiple characters, they may overlap with each other and share characters.

Example(s)
strDist("catcowcat", "cat") == 9
strDist("catcowcat", "cow") == 3
strDist("cccatcowcatxx", "cat") == 9
strDist("ooowhwhwooo", "whw") == 5
 

🔎 EXPLORE
List your assumptions & discoveries:

-  sub > word -> base case
-  iterate 1 char at a time
-  start counting when word[0:len(sub)] == sub  
 

Insightful & revealing test cases:

 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function strDist(word, sub) {
def strDist(word: str,  sub: str) -> int:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

def strDist(word: str,  sub: str) -> int:
    
    
    
    # base case
    if len(word) < len(sub):
        return 0
    
    # base case if wird starts and ends with sub
    if word[0:len(sub)] == sub and word[len(word)-len(sub):] == sub:
        return len(word)


    # removing from front
    if word[0:len(sub)] != sub: 
        return strDist(word[1:], sub)
    
    # removing from back
    return strDist(word[0:len(word)-1],sub)


print(strDist("catcowcat", "cat") == 9 )
print(strDist("catcowcat", "cow")  == 3 )
print(strDist("cccatcowcatxx", "cat")  == 9 )
print(strDist("abccatcowcatcatxyz", "cat") == 12)
print(strDist("ooowhwhwooo", "whw") == 5)
print(strDist("xyx", "x") == 3)
print(strDist("xyx", "y") == 1)
print(strDist("xyx", "z") == 0)
print(strDist("z", "z") == 1)
print(strDist("x", "z") == 0)
print(strDist("", "z") == 0)
print(strDist("hiHellohihihi", "hi") == 13)
print(strDist("hiHellohihihi", "hih") == 5)
print(strDist("hiHellohihihi", "o") == 1)
print(strDist("hiHellohihihi", "ll") == 2)

