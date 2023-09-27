
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
- terminating base case: LL node is None: return 0
- no nodes. return 0

test cases:
- even # of nodes
- odd # of nodes
- empty LL
- 1 node
- multiple maxes? 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1: traverse through LL recursively and compare the node values with node.next values
Time: O(N)
Space: O(N)
 

📆 PLAN
Outline of algorithm #: 
- base case: if your at end of LL, return float('-inf')
- compare values

🛠️ IMPLEMENT
Write your algorithm.
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
class ListNode:
    def __init__(self, value = 0, next = None): 
        self.value = value
        self.next = next

  #iterative      
# def findMax(node: ListNode) -> int:
    
#     max = float("-inf")
#     while node != None:
#         max = node.value if node.value > max else max

#         node = node.next

#     return max

# recursive 
def findMax(node: ListNode) -> int:
    
    
    if node is None:
        return 0
    
    if node.next is None:
        return node.value
    

    return max(node.value, findMax(node.next))

LL1 = ListNode(1, ListNode(4, ListNode(5, ListNode(1))))
LL2 = ListNode(7, ListNode(1, ListNode(5, ListNode(1))))
LL3 = ListNode(-1, ListNode(-3, ListNode(-5, ListNode(0, ListNode(-11)))))
print(findMax(LL1)) # 5
print(findMax(LL2)) # 7
print(findMax(LL3)) # 0
print(findMax(ListNode(1))) # 1