"""


🔎 EXPLORE
What are some other insightful & revealing test cases?
- if no Nodes: return 0


🧠 BRAINSTORM
What approaches could work?
Algorithm 1: thinking recursively, I want to pass a node and a accumulator var into the function
    keeps count of number of nodes and traverses through LL
    if node.next is None, return accumulator
Time: O(N) 
Space: O(N)
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
Write your algorithm.
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.


▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
✏️ Description
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Q. Given an unsorted linked list, count the number of elements (iteratively or recursively).

Examples:
• Given a linked list: 1 ➞ 4 ➞ 5 // returns 3
• Given a linked list: 0 // returns 1

▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
🟦 Python
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
class ListNode:
    def __init__(self, value = 0, next = None): 
        self.value = value
        self.next = next
    
def count(node: ListNode) -> int:
    # Write your code here.
    pass

# Test Cases
LL1 = ListNode(1, ListNode(4, ListNode(5)))
print(count(None)) # 0
print(count(LL1)) # 3
print(count(ListNode())) # 1

"""

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def count(head) -> int:
    
    if head is None:
        return 0 
    
    return 1 + count(head.next)

LL1 = ListNode(1, ListNode(4, ListNode(5)))
print(count(None)) # 0
print(count(LL1)) # 3
print(count(ListNode())) # 1