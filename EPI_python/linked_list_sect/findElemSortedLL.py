'''

▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Q. Given a sorted linked list of unique integers, check if the list contains an element with a target value.

Examples:
• Given a linked list: 2 ➞ 3 ➞ 5, target: 2 // returns True
• Given a linked list: 2 ➞ 3 ➞ 5, target: 4  // returns False

▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
🟦 Python
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
class ListNode:
    def __init__(self, value = 0, next = None): 
        self.value = value
        self.next = next

def search(head: ListNode, target: int) -> bool: 
    # Write your code here.
    pass

# Test Cases
LL1 = ListNode(1, ListNode(2, ListNode(3, ListNode(5, ListNode(6, ListNode(7, ListNode(10)))))))
print(search(None, 1)) # False
print(search(LL1, 2)) # True
print(search(LL1, 4)) # False
print(search(LL1, -1)) # False
print(search(LL1, 10)) # True
print(search(LL1, 11)) # False


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
    def __init__(self, val, next = None):
        self.val = val
        self.next = next



def search(head: ListNode, target: int) -> bool: 
        
    if not head:
        return False
        
    else:
        curr = head

        while curr:
            if curr.val == target:
                return True
            else:
                curr = curr.next
            
        return False
        

        

LL1 = ListNode(1, ListNode(2, ListNode(3, ListNode(5, ListNode(6, ListNode(7, ListNode(10)))))))
print(search(None, 1)) # False
print(search(LL1, 2)) # True
print(search(LL1, 4)) # False
print(search(LL1, -1)) # False
print(search(LL1, 10)) # True
print(search(LL1, 11)) # False
