

'''
❓ PROMPT
We have a number of bunnies, each with two big floppy ears. We want to compute the total number of ears across all the bunnies recursively,
 without loops or multiplication.

Example(s)
bunnyEars(3) == 6
bunnyEars(5) == 10
 

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
function bunnyEars(bunnies) {
def bunnyEars(bunnies: int) -> int:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
def bunnyEars(bunnies: int) -> int:
    if bunnies == 0:
        return 0
    
    return 2 + bunnyEars(bunnies - 1)


print(bunnyEars(12) == 24)
print(bunnyEars(10) == 20)
print(bunnyEars(5) == 10)
print(bunnyEars(3) == 6)
print(bunnyEars(2) == 4)
print(bunnyEars(1) == 2)
print(bunnyEars(0) == 0)