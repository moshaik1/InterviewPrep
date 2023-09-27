

'''
❓ PROMPT
Given a string, recursively compute a new string where identical chars that are 
adjacent in the original string are separated from each other by a "*".

Example(s)
pairStars("hello") == "hel*lo"
pairStars("xxyy") == "x*xy*y"
pairStars("aaaa") == "a*a*a*a"
 

🔎 EXPLORE
List your assumptions & discoveries:
 

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function pairStars(word) {
def pairStars(word: str) -> str:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

def pairStars(word: str) -> str:

    if len(word) <= 1:
        return word
    
    if word[0] == word[1]:
        return word[0] + "*" + pairStars(word[1:])
    
    return word[0] + pairStars(word[1:])


print(pairStars("hello") == "hel*lo")
print(pairStars("xxyy") == "x*xy*y")
print(pairStars("aaaa") == "a*a*a*a")
print(pairStars("aaab") == "a*a*ab")
print(pairStars("aa") == "a*a")
print(pairStars("a") == "a")
print(pairStars("") == "")
print(pairStars("noadjacent") == "noadjacent")
print(pairStars("abba") == "ab*ba")
print(pairStars("abbba") == "ab*b*ba")