

'''
❓ PROMPT
A bug in the Formation session tool accidentally duplicated some Fellows in sessions. Given an array of names representing Fellows in a session, return an array of the distinct Fellows. The array must be in the same order as the input.

Follow-up question:
How would removing the Fellows in place, instead of using a new output array, affect the algorithm's runtime?

Example(s)
["oliver", "pixel", "oliver", "pinky"] => ["oliver", "pixel", "pinky"]
 

🔎 EXPLORE
List your assumptions & discoveries:

-empty? 
 

Insightful & revealing test cases:


 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1: adding all of the elements to a set and converting the set back into an array
Time: O(n)
Space: O(n)
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function removeDuplicateFellows(fellows) {
def removeDuplicateFellows(fellows: list[str]) -> list[str]:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

def removeDuplicateFellows(fellows: list[str]) -> list[str]:

    # answer = set(fellows)

    # return list(answer)

    answer = []
    fellowSet = set()

    for fellow in fellows:
        if fellow not in fellowSet:
            fellowSet.add(fellow)
            answer.append(fellow)

    return answer

print(removeDuplicateFellows(["oliver", "pixel", "oliver", "pinky"]))