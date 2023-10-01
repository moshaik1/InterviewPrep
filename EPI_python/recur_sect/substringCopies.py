

'''
❓ PROMPT
Given a string and a non-empty substring *sub*, compute recursively if at least n copies of sub appear in the string somewhere,
possibly with overlapping. N will be non-negative.

Example(s)
strCopies("catcowcat", "cat", 2) == True
strCopies("catcowcat", "cow", 2) == False
strCopies("catcowcat", "cow", 1) == True
 

🔎 EXPLORE
List your assumptions & discoveries:
- if string is empty, return 0?
- at least n copies!

Insightful & revealing test cases:
- overlapping case: strCopies("wowowow" , "wow", 2) == True
- empty string
- count is lower than N
- count is higher than N
- no occurance of substring

 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1: base case would be an empty string, return 0 oppurances. 
Time: O()
Space: O()
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function strCopies(word, sub, n) {
def strCopies(word: str, sub: str, n: int) -> bool: 
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
def strCopies(word: str, sub: str, n: int) -> bool: 

    if n == 0:
        return True
    if len(word) < len(sub):
        return False
    
    if word[0:len(sub)] == sub:
       return strCopies(word[1:], sub, n-1)
    
    return strCopies(word[1:], sub, n)

   

    
    
def strCopies(word: str, sub: str, n: int) -> bool:
  if n == 0:
    return True

  if len(word) < len(sub):
    return False

  if word[0:len(sub)]==sub:
    return strCopies(word[1:], sub, n - 1)

  return strCopies(word[1:], sub, n)

print(strCopies("catcowcat", "cat", 2) == True)
print(strCopies("catcowcat", "cow", 2) == False)
print(strCopies("catcowcat", "cow", 1) == True)
print(strCopies("iiijjj", "i", 3) == True)
print(strCopies("iiijjj", "i", 4) == False)
print(strCopies("iiijjj", "ii", 2) == True)
print(strCopies("iiijjj", "ii", 3) == False)
print(strCopies("iiijjj", "x", 3) == False)
print(strCopies("iiijjj", "x", 0) == True)
print(strCopies("iiiiij", "iii", 3) == True)
print(strCopies("iiiiij", "iii", 4) == False)
print(strCopies("ijiiiiij", "iiii", 2) == True)
print(strCopies("ijiiiiij", "iiii", 3) == False)
print(strCopies("dogcatdogcat", "dog", 2) == True)