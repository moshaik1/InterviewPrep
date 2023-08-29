

"""
Singly Linked List:

INSERTING: O(1) -> as long as we have a reference to the node location
DELETION:  O(1) -> as long as we have a reference to the node location
TRAVERSING: O(N)
SEARCHING: O(N)


node.next used to reference next node
node.next.next used to delete next node and reference next next node

head used to reference 1st element
tail used to reference last element

last element points to null

"""

class ListNode:
    def __init__(self , data ):
        self.data = data
        self.next = None


node1 = ListNode(10)
node2 = ListNode(20)
node1.next = node2
curr = node1

while curr:
    print(curr.data)
    curr = curr.next

if not curr:
    print("None")