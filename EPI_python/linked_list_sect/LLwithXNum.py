

'''
❓ PROMPT
Given integers *X* and *Y*, return the head of a linked list with *X* nodes with value *Y*.

Example(s)
createLL(5, 3)
"3 -> 3 -> 3 -> 3 -> 3"

createLL(6, 6)
"6 -> 6 -> 6 -> 6 -> 6 -> 6"

createLL(2, -10)
"-10 -> -10"
 

🔎 EXPLORE
List your assumptions & discoveries:
 (0, number)-> return None?
 negative x? NO
Insightful & revealing test cases:
 (0 , 5) 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O(X)
Space: O(X)
 

📆 PLAN
Outline of algorithm #: 
(4 , 6)

- create a count variable that keeps track of LL length
- while counter <= count
    - create a new node with the value of val and connect it to curr node

 

🛠️ IMPLEMENT
function createLL(count, value) {
def createLL(count: int, val: int) -> Node:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def createLL(count: int, val: int) -> Node:
    
    if count == 0:
        return None
    
    else:
        counter = 1
        head = Node(val)
        curr = head
        while counter < count:
            curr.next = Node(val)
            curr = curr.next
            counter += 1

    return head
    

def toString(head: Node) -> None:
  if not head:
    return "<empty>"

  parts = []
  while head:
    parts.append(str(head.val))
    head = head.next

  return " -> ".join(parts)

print(toString(createLL(0, 1000)) == "<empty>")
print(toString(createLL(1, 999)) == "999")
print(toString(createLL(2, 88)) == "88 -> 88")
print(toString(createLL(3, 4)) == "4 -> 4 -> 4")
print(toString(createLL(5, 3)) == "3 -> 3 -> 3 -> 3 -> 3")
print(toString(createLL(6, 6)) == "6 -> 6 -> 6 -> 6 -> 6 -> 6")
print(toString(createLL(2, -10)) == "-10 -> -10")
print(toString(createLL(3, 0)) == "0 -> 0 -> 0")