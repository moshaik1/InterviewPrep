

'''
▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
✏️ Description
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Q. Given a linked list, sum all elements in the list.

Examples:
• Given a linked list: 1 ➞ 4 ➞ 5 // returns 10
• Given a linked list: 1 // returns 1

▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
🟦 Python
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
class ListNode:
    def __init__(self, value = 0, next = None): 
        self.value = value
        self.next = next
        
def sum(node: ListNode) -> int:
    # Write your code here.
    pass

# Test Cases
LL1 = ListNode(1, ListNode(4, ListNode(5)))
print(sum(None)) # 0
print(sum(LL1)) # 10
print(sum(ListNode(1))) # 1


🔎 EXPLORE
What are some other insightful & revealing test cases?
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()
 

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
        
def sum(node: ListNode) -> int:
    
    sumTot = 0

    while node:
        sumTot = sumTot + node.value
        node = node.next

    return sumTot

LL1 = ListNode(1, ListNode(4, ListNode(5)))
print(sum(None)) # 0
print(sum(LL1)) # 10
print(sum(ListNode(1))) # 1
