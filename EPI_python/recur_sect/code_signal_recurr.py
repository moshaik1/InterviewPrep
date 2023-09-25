
"""
Given a linked list of integers and a number, k, add k to every kth node starting from the end. For example, if the list is [1 -> 2 -> 3 -> 4] and k is 3, then the result is [1 -> 5 -> 3 -> 4]. The 2 was the third value from the end, we added three to get 5. No other nodes are modified.

For a longer example, consider the list:

[1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7]
If k=3, two nodes change:

[1 -> 5 -> 3 -> 4 -> 8 -> 6 -> 7]
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] linkedlist.integer head

[input] integer k

[output] linkedlist.integer

"""

# Singly-linked lists are already defined with this interface:
class ListNode(object):
  def __init__(self, x, next=None):
    self.value = x
    self.next = next

def solution(head:ListNode):
    curr = head

    if curr is None:
       return 0

    return 1 + solution(curr.next)
        

node1 = ListNode(2, ListNode(4, ListNode(1, ListNode(3, ListNode(8, ListNode(5))))))
print(solution(node1))



"""
Determine if a number, n, is a power of some other number k. Return the exponent. 
For example, for n = 9 and k = 3, return 2 because 3 to the power of 2 is 9. If n is not a power of k, return -1.

We will not be testing with negative values or exponents and k will be greater than 1.

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] integer n

[input] integer k

[output] integer
"""

def solution(n, k):
   
    if n == 1:
        return 0

    return  1 + solution(n / k , k) if n % k == 0 else -2

print(solution(9,3))
print(solution(27,3))
print(solution(99,9))
print(solution(81,9))
"""
Write a recursive function that takes a linked list and returns the minimum and maxumum value in an array, minimum first, then maximum. For example:

1 -> 2 -> 3
returns '[1, 3]`

You may not assume the list is sorted. The list will not be empty.

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] linkedlist.integer head

[output] array.integer


"""

# Singly-linked lists are already defined with this interface:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def solution(head):

    answer = [float('inf'),float('-inf')]

    if head is None:
       return answer

    if head.value > answer[0]  :
       return 