




class ListNode:
    def __init__(self, value = 0, next = None): 
        self.value = value
        self.next = next

def arrayify(head) -> [int]:
    array = []
    ptr = head
    while ptr != None:
        array.append(ptr.value)
        ptr = ptr.next
    return array
        
# 1 -> 2 -> 3 -> 4 -> 5 -> None

def reverse(head:ListNode)->ListNode:

    prev = None
    curr = head

    if head is None or head.next is None:
        return head

    while curr:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode

    return prev


# Test Cases
LL1 = ListNode(13, ListNode(1, ListNode(5, ListNode(3, ListNode(7, ListNode(10))))))
print(arrayify(reverse(ListNode(1)))) # [1]
print(arrayify(reverse(ListNode(1, ListNode(2))))) # [2, 1]
print(arrayify(reverse(LL1))) # [10, 7, 3, 5, 1, 13]
print(reverse(None)) # None


