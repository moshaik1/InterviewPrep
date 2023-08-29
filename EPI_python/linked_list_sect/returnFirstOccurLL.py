

'''
❓ PROMPT
Given a linked list and a target value, return the index of the first occurrence of that value in the linked list. The index should be zero-indexed.

Example(s)
list1 = 1 -> 2 -> 3 -> 4 -> 5

firstIndexInLL(list1, 9) == -1
firstIndexInLL(list1, 3) == 2
 

🔎 EXPLORE
List your assumptions & discoveries:

- if linked list is empty, no nodes, return -1

 

Insightful & revealing test cases:
- empty linked list
- 1 node thas target
- 1 node that not target
- multple unique nodes 
- multple nodes with multiple target nodes
- multiple nodes with no target node
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1: have a index variable to keep track of index, and a curr to keep track of current node. Iterate through linked list to find target.
            if no target is found or linked list is empty, return -1
Time: O(n)
Space: O(1) since youre only storing a single variable
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function firstIndexInLL(node, target) {
def firstIndexInLL(node: Node, target: int) -> int:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


def firstIndexInLL(node: Node, target: int) -> int:

    if not node:
        return -1
    
    
    index = 0
    
    while node:
            
        if node.data == target:
            return index
        
        index += 1    
        node = node.next
        

        
    return -1


list1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
list2 = Node(2)
list3 = Node(-1, Node(-2, Node(-3, Node(-4, Node(-5)))))
list4 = Node(1, Node(2, Node(3, Node(2, Node(1)))))

print(firstIndexInLL(None, 12) == -1)
print(firstIndexInLL(list1, 9) == -1)
print(firstIndexInLL(list1, 3) == 2)
print(firstIndexInLL(list2, 2) == 0)
print(firstIndexInLL(list2, 1) == -1)
print(firstIndexInLL(list3, -2) == 1)
print(firstIndexInLL(list4, 2) == 1)
print(firstIndexInLL(list4, 1) == 0)

