
'''
❓ PROMPT
Given a linked list, return the number of values that occur exactly twice. This is the linked list version of a problem you may have seen in the hash structures Subchallenge so might be familliar!

Example(s)
head = 1 -> 2 -> 2 -> 3 -> 3 -> 3
numPairs(head) == 1
 

🔎 EXPLORE
List your assumptions & discoveries:
- is the LL already sorted?
- empty LL return 0?

 

Insightful & revealing test cases:
- empty
- 1 node
- 1 pair
- multiple pairs
- not sorted

 head = 1 -> 5 -> 2 -> 5 -> 3 -> 3

🧠 BRAINSTORM
What approaches could work? 
Algorithm 1: iterate through LL and populate Hashmap.
 then iterate through hashmap with an accumulator variable that counts pairs
Time: O(n)
Space: O(n)
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function numPairs(head) {
def numPairs(head: Node) -> int:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def numPairs(head: Node) -> int: 

    pairCounter = {}

    curr = head
    answer = 0

    while curr:

        if curr.val not in pairCounter:
            pairCounter[curr.val] = 1
        else:
            pairCounter[curr.val] = pairCounter.get(curr.val) + 1

        curr = curr.next
    

    for val in pairCounter.values():
        if val == 2:
            answer += 1

    return answer


head1 = Node(1, Node(2, Node(2, Node(3, Node(3, Node(3))))))
head2 = Node(5, Node(5, Node(10, Node(20))))
head3 = Node(5, Node(5, Node(10, Node(10))))
head4 = Node(5, Node(5, Node(5, Node(10))))
head5 = Node(5, Node(10, Node(10, Node(10))))
head6 = Node(4)
head7 = Node(5, Node(5))
head8 = Node(5, Node(5, Node(5, Node(5))))
head9 = Node(6, Node(9))
head10 = Node(5, Node(5, Node(5, Node(10, Node(10)))))
head11 = Node(6, Node(5, Node(5, Node(5, Node(5, Node(6))))))

print(numPairs(None) == 0)
print(numPairs(head1) == 1)
print(numPairs(head2) == 1)
print(numPairs(head3) == 2)
print(numPairs(head4) == 0)
print(numPairs(head5) == 0)
print(numPairs(head6) == 0)
print(numPairs(head7) == 1)
print(numPairs(head8) == 0)
print(numPairs(head9) == 0)
print(numPairs(head10) == 1)
print(numPairs(head11) == 1)