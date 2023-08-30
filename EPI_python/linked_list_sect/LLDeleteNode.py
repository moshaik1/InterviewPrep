
'''
🔎 EXPLORE
What are some other insightful & revealing test cases?

Guarantees:
    - node(target) will not be the last node in the linked list
    - node(target) is an anctual node in the linked list

    - input will be a linked list and a target node
    - output will be entire list after calling function

* since we dont have a pointer to the previous node, we cant
 actually remove it in the traditional way

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

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def deleteNode(self, node):

        # 4 -> 1 -> 9 -> none

        node.val=node.next.val
        node.next=node.next.next

        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """