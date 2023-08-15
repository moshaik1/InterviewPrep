
"""
/*
'''
❓ PROMPT
Problem Statement: Write a function that takes an array and reverses its elements in place. Do not use built-in methods!

Daniel on two-pointer problems: https://drive.google.com/file/d/1VattL0rWv3AUkGU3njhhfuOh24pMFSjr/view

This task is a basic introduction to what is commonly called "two pointer" algorithms. They come up often when dealing with data ordered or organized in some way or when we're trying to do something with the ordering.

This problem is the latter. The order of the elements in the array at the start doesn't matter, but the task is to re-organize the elements so that at the end, the order is the reverse of what it was coming in.

Example(s)
reverse([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
 

🔎 EXPLORE
List your assumptions & discoveries:

- empty?

 

Insightful & revealing test cases:
print(reverse( [] ))
print(reverse( [ 5 ] ))
print(reverse( [ 1 , 2 , 3 , 4] ))
print(reverse( [ 1 , 2 , 3 , 4 , 5] ))

 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1: 2 pointer approach, with 1 pointer at the head and 1 pointer at the tail, and swap
Time: O(1)
Space: O(1)
 

📆 PLAN
Outline of algorithm #: 


 

🛠️ IMPLEMENT
function reverse(array) {
def reverse(array: list[int]) -> list[int]:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
*/
"""

def reverse(array : list[int]) -> list[int]:


    if not array:
        return []
    else:
        head = 0
        tail = len(array)-1

        while head < tail:
            array[head],array[tail] = array[tail], array[head]
            head += 1
            tail -= 1




    
        return array

print(reverse( [] ))
print(reverse( [ 5 ] ))
print(reverse( [ 1 , 2 , 3 , 4] ))
print(reverse( [ 1 , 2 , 3 , 4 , 5] ))