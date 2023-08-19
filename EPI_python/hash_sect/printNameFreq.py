
'''
❓ PROMPT
You're given a comma-separated string of names, and you want to print how many times each name appeared. For each person that appears, you should print a string *{name} appeared {x} times.*, in order of appearance.

To properly compare results in the test suite, return an array of strings joined by a newline as the result of your method.

return myArr.join("\n") // js
return "\n".join(myArr) # py

Example(s)
printNameFreq("Tony, Jessica, Paavo, Jessica, Tony, Zoe") ==
Tony appeared 2 times.
Jessica appeared 2 times.
Paavo appeared 1 time.
Zoe appeared 1 time.

printNameFreq("") == "Nobody appeared."
 

🔎 EXPLORE
List your assumptions & discoveries:
 

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work? 
Algorithm 1: string -> array of names -> iterate through array and populate dictionary with {key:name, value:occurrance}
Time: O(n)
Space: O(n)
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function printNameFreq(names) {
def printNameFreq(names: str) -> str:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

def printNameFreq(names: str) -> str:

    if not names:
        return "nobody appeared."

    arr = names.split(', ')
    answer = []
    nameDict = {}

    for name in arr:
        if name in nameDict:
            nameDict[name] += 1
        else:
            nameDict[name] = 1
        
    
    while len(nameDict) > 0:
        maxVal = float("-inf")
        maxName = ""
        for name, occur in nameDict.items():
            if occur > maxVal:
                maxVal = occur
                maxName = name

        answer.append(f"{maxName} appeared {maxVal} time{'s' if maxVal > 1 else ''}.")
        nameDict.pop(maxName,maxVal)

    return "\n".join(answer)
            

print(printNameFreq("Tony, Jessica, Paavo, Jessica, Tony, Zoe"))
print("-----------------------------------------------------")
print(printNameFreq("") 
== "nobody appeared."
      )
print("-----------------------------------------------------")
print(printNameFreq("Tony") 
      == "Tony appeared 1 time."
      )
print("-----------------------------------------------------")
print(printNameFreq("Tony, Jessica") 
      == 
"Tony appeared 1 time.\n\
Jessica appeared 1 time."
)
print("-----------------------------------------------------")
print(printNameFreq("Tony, Tony, Tony") 
      == "Tony appeared 3 times."
      )
print("-----------------------------------------------------")
print(printNameFreq("Tony, Jessica, Paavo, Zoe") 
      == 
"Tony appeared 1 time.\n\
Jessica appeared 1 time.\n\
Paavo appeared 1 time.\n\
Zoe appeared 1 time."
)
print("-----------------------------------------------------")
print(printNameFreq("Tony, Jessica, Paavo, Jessica, Tony, Zoe") 
      == 
"Tony appeared 2 times.\n\
Jessica appeared 2 times.\n\
Paavo appeared 1 time.\n\
Zoe appeared 1 time."
)



