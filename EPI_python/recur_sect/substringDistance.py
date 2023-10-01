

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

def strDist(word: str,  sub: str, flag = False) -> int:
    #flag = False
    subLength = len(sub)
    counter = 0

    if len(word) < subLength:
        print("reached end")
        return 0
    

    if word[0:subLength] == sub and flag is False: 
        #flag = True
        counter += 1
        print("counter = " + counter)
        return 1 + strDist(word[1:], sub, True)

    if word[0:subLength] == sub and flag is True:
        #flag = False
        counter += subLength
        print("counter + sub = " + counter)
        return subLength + strDist(word[subLength:], sub, False)
    
    
    return strDist(word[1:],sub, False )


print(strDist("catcowcat", "cat")) # == 9)
# print(strDist("catcowcat", "cow")) # == 3)
# print(strDist("cccatcowcatxx", "cat")) # == 9)
# print(strDist("abccatcowcatcatxyz", "cat") == 12)
# print(strDist("ooowhwhwooo", "whw") == 5)
# print(strDist("xyx", "x") == 3)
# print(strDist("xyx", "y") == 1)
# print(strDist("xyx", "z") == 0)
# print(strDist("z", "z") == 1)
# print(strDist("x", "z") == 0)
# print(strDist("", "z") == 0)
# print(strDist("hiHellohihihi", "hi") == 13)
# print(strDist("hiHellohihihi", "hih") == 5)
# print(strDist("hiHellohihihi", "o") == 1)
# print(strDist("hiHellohihihi", "ll") == 2)


"""

catcowcatcowcat -> answer is 15



"""