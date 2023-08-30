
'''
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

🔎 EXPLORE
What are some other insightful & revealing test cases?
 - empty linked list
 - even number of nodes
 - odd number of nodes
 - 1 node

🧠 BRAINSTORM
What approaches could work?
Algorithm 1: have an accumulator variable that counts nodes
Time: O(n)
Space: O(n)
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
Write your algorithm.
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
class ListNode:
    def __init__(self, value = 0, next = None): 
        self.value = value
        self.next = next
    
def count(node: ListNode) -> int:
    counter = 0 
    while node:
        counter += 1
        node = node.next
    
    return counter

LL1 = ListNode(1, ListNode(4, ListNode(5)))
print(count(None)) # 0
print(count(LL1)) # 3
print(count(ListNode())) # 1
