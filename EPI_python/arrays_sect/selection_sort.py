
'''
🔎 EXPLORE
What are some other insightful & revealing test cases?
- empty? 
- multiples of an element?

- [ ]
- [ 3 , 2 , 1]
- [ 5 , 3 , 2 , 1]
- [ 1 ]
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O(n^2)
Space: O(1)
 

📆 PLAN
Outline of algorithm #: 

 - have an outer loop that iterates as long as i < len(array)
 - have an inner loop with pointer j thats checks to see if j is smaller than j-1, if so swap; else, iterate outer loop
 - if swap occurs, swap j-1 with j, then check if j is less than j-1, if so swap again. continue to swap until j is greater than j+1 or j >= 1
 

🛠️ IMPLEMENT
Write your algorithm.
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
"""
 [ 4 , 6 , 8 , 3 , 1 , 9 , 5 ]
       j  i 
"""

# def selectionSort( arr:list[int]) -> list[int]:

#     for i in range(1 , len(arr)):

#         j = i
#         while j >= 1:
#             #swap
#             if arr[j] < arr[j-1]:
#                 arr[j], arr[j-1] = arr[j-1],arr[j]
#                 j -= 1
#             else:
#                 break

#     return arr

##### SELECTION SORT ORGANIZES BASED ON THE MINIMUM VALUE. ITERATES THROUGH THE WHILE ARRAY AND FINDS THE MINUMUM VALUE, AT THE END SWAPS MINIMUM WITH i, 
            
def selectionSort(list1):

    for i in range(0 , len(list1)-1):

        minVal = i

        for j in range(i + 1, len(list1)):
            if list1[minVal] > list1[j]:
                minVal = j

        list1[i],list1[minVal] = list1[minVal],list1[i]

    return list1


print(selectionSort([ 4 , 6 , 8 , 3 , 1 , 9 , 5 ]))
print(selectionSort([ 4 , 6 , 8 , 3 , 1 , 9 , 5 , 0 ]))
print(selectionSort([ 4 ]))
print(selectionSort([ ]))
print(selectionSort([ 4 , 6 , 8 , 3 , 1 , 9 , 5 , 1]))