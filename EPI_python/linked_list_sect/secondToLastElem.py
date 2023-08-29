
'''
❓ PROMPT
Given a linked list, return the second to last element's value.

Example(s)
1 -> 2 => 1
1 -> 2 -> 3 -> 4 => 3
 

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
function secondToLast(head) {
def secondToLast(head: Node) -> int:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def secondToLast(head: Node) -> int:

    if not head or head.next == None:
        return None
    
    while head.next.next != None:
            
        head = head.next

            
    return head.val


print(secondToLast(None) == None)

# 1
head = Node(1)
print(secondToLast(head) == None)

# 1 -> 2
head = Node(1, Node(2))
print(secondToLast(head) == 1)

# 1 -> 2 -> 3
head = Node(1, Node(2, Node(3)))
print(secondToLast(head) == 2)

# 1 -> 2 -> 3 -> 4
head = Node(1, Node(2, Node(3, Node (4))))
print(secondToLast(head) == 3)

# 1 -> 2 -> 3 -> 4 -> 5
head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(secondToLast(head) == 4)