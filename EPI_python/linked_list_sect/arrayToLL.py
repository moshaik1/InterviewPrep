
'''
❓ PROMPT
Given an array containing numbers, convert this to a singly linked list and return the head of the list.

Example(s)
arrayToLL([1,2]) == "1 -> 2"
arrayToLL([1,2,3]) == "1 -> 2 -> 3"
 

🔎 EXPLORE
List your assumptions & discoveries:
- empty array? returns None
 

Insightful & revealing test cases:
- array of 1 element
- array of even elements
- array of odd elements
- empty array
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1: iterating through an array, and creating a node of each element until you hit the end of the array
Time: O(n) iterating through an array of size n
Space: O(n) since youre storing n elements into nodes
 

📆 PLAN
Outline of algorithm #: 

-create a dummy node in a variable and a curr variable that points to dummy
-iterate though the array, creating a new node for every element using the curr variable
to connect nodes
-return dummy.next since its the head


 

🛠️ IMPLEMENT
function arrayToLL(array) {
def arrayToLL(array: list[int]) -> Node:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

class Node:
    def __init__(self, val , next=None):
        self.val = val
        self.next = next


def arrayToLL(array: list[int]) -> Node:

    

    sentinal = Node(0)
    curr = sentinal

  
    for i in range(len(array)):
        
        curr.next = Node(array[i])
        curr = curr.next

    return sentinal.next




def toString(head: Node) -> None:
  if not head:
    return "<empty>"

  parts = []
  while head:
    parts.append(str(head.val))
    head = head.next

  return " -> ".join(parts)


print(toString(arrayToLL([])) == "<empty>")
print(toString(arrayToLL([1])) == "1")
print(toString(arrayToLL([1,2])) == "1 -> 2")
print(toString(arrayToLL([1,2,3])) == "1 -> 2 -> 3")
print(toString(arrayToLL([5,0,3])) == "5 -> 0 -> 3")
print(toString(arrayToLL([8,7,8,8])) == "8 -> 7 -> 8 -> 8")
print(toString(arrayToLL([8,7,8,8,7])) == "8 -> 7 -> 8 -> 8 -> 7")