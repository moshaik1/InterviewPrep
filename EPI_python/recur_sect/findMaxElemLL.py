


'''
▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
✏️ Description
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Q. Given an unsorted linked list, find the element with the largest value.

Examples:
• Given a linked list: 1 ➞ 4 ➞ 5 ➞ 1 // returns 5
• Given a linked list: 1  // returns 1

▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
🟦 Python
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
class ListNode:
    def __init__(self, value = 0, next = None): 
        self.value = value
        self.next = next
        
def findMax(node: ListNode) -> int:
    # Write your code here.
    pass

# Test Cases
LL1 = ListNode(1, ListNode(4, ListNode(5, ListNode(1))))
LL2 = ListNode(7, ListNode(1, ListNode(5, ListNode(1))))
LL3 = ListNode(-1, ListNode(-3, ListNode(-5, ListNode(0, ListNode(-11)))))
print(findMax(LL1)) # 5
print(findMax(LL2)) # 7
print(findMax(LL3)) # 0
print(findMax(ListNode(1))) # 1

🔎 EXPLORE
What are some other insightful & revealing test cases?
- LL is empty, return 0?
- LL only has 1 element, return value of the node

🧠 BRAINSTORM
What approaches could work?
Algorithm 1: traverse through linked list recursively, base case: if node is None: return 0. if node.next is None: return node.value
Time: O(n) -> since youre traversing through the whole array
Space: O(1)
 

📆 PLAN
Outline of algorithm #: 
10 -> 1 -> 5 -> 11 -> 4
 

🛠️ IMPLEMENT
Write your algorithm.
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
class ListNode:
    def __init__(self, value,next=None):
        self.value = value
        self.next = next

# def findMax(node: ListNode) -> int:
    
#     if node is None:
#         return 0
#     if node.next is None:
#         return node.value
    
#     return max(node.value, findMax(node.next))

def findMax(node: ListNode) -> int:

    if node is None:
        return 0
    
    maxVal = float("-inf")

    while node:
        maxVal = max(maxVal , node.value)
        node = node.next
    return maxVal

LL1 = ListNode(1, ListNode(4, ListNode(5, ListNode(1))))
LL2 = ListNode(7, ListNode(1, ListNode(5, ListNode(1))))
LL3 = ListNode(-1, ListNode(-3, ListNode(-5, ListNode(0, ListNode(-11)))))
print(findMax(LL1)) # 5
print(findMax(LL2)) # 7
print(findMax(LL3)) # 0
print(findMax(ListNode(1))) # 1