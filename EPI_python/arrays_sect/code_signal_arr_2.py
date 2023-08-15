
"""
1Q. Given two integer arrays of equal length, merge them into one by taking the minimum value at the each index.

Example:
Inputs: [1, 2, 3, 4, 5] and [5, 4, 3, 2, 1]
Output:[1, 2, 3, 2, 1] // at the index 0, 1 is smaller than 5. Thus, take 1 as the first element.
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer a1

[input] array.integer a2

[output] array.integer

--------CORRECT-----------------------------------------------------------
"""

# def solution(a1, a2):
    
#     if not a1:
#         return []
    
    
#     for i in range(0,len(a1)):
#         if a1[i] <= a2[i]:
#             continue
            
#         else:
#             a1[i] = a2[i]
            
            
#     return a1



"""
2Q. Given an array of integers where all but one adjacent pair has been swapped (unsorted), fix the array by swapping back the broken pair.

Example:
Input: [1, 2, 3, 5, 4, 6]
Output: [1, 2, 3, 4, 5, 6]
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer array

[output] array.integer


--------CORRECT-----------------------------------------------------------
"""

# def solution(array):
    
#     if not array:
#         return []
        
#     else:
        
#         for i in range(0,len(array)-1):
            
#             if array[i] > array[i+1]:
#                 array[i], array[i+1] = array[i+1],array[i]
#                 return array
    
#     return array


"""
3Q. Given an array of integers, move all negative numbers to the left in the order they appear.

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer array

unsorted array

[output] array.integer

sorted array

--------CORRECT-----------------------------------------------------------
"""

# def solution(array):
    
#     if not array:
#         return []
    
#     elif len(array) == 1:
#         return array
        
#     else:
        
#         answer = []
        
#         for i in range(0, len(array)):
#             if array[i] < 0:
#                 answer.append(array[i])
        
#         for j in range(0,len(array)):
#             if array[j] >= 0:
#                 answer.append(array[j])
        
        
            
#         return answer
                



"""
4Q. Given a sorted array of integers and a target value, insert the target into the array in the appropriate location. You may assume there are no duplicates.

Example:
Input: array = [1, 2, 4, 5, 6], target = 3
Output: [1, 2, 3, 4, 5, 6]
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer array

[input] integer target

[output] array.integer
--------WRONG-----------------------------------------------------------
"""

# def solution(array, target):
    
    
#     answer = []
    
#     if not array:
#         array.append(target)
#         return array
    
    
#     elif target > array[len(array)-1]:
#         array.append(target)
#         return array
        
#     elif target < array[0]:
#         answer.append(target)
#         answer += answer + array[1:]
#         return answer 
    
#     else:   
#         for i in range(len(array)-1):
            
#             if abs(target - array[i]) <= abs(target - array[i+1]):
                
#                 answer.append(i)
#                 answer.append(target)
                
            
#             else: 
#                 answer.append(i)
            
#     return answer
        
        
        
        
        
    
    



"""
5Q. Create an array of integers with a starting number s, an increment value i, and a repetition count r given.

Examples:
Input1: start = 3, increment = 2, repetition count = 5
Output1: [3, 5, 7, 9, 11]
Input2: start = 1, increment = 1, repetition = 3
Output2: [1, 2, 3]
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] integer s

starting value

[input] integer i

increment value

[input] integer r

repetition count

[output] array.integer
--------CORRECT-----------------------------------------------------------
"""

# def solution(s, i, r):

#     # array = []
    
    
#     arry = [ s + (i*j)  for j in range(0,r)]
#     return arry

#     # for j in range(0,r):
#     #     array.append(s + (i*j) )
        
#     # return array

"""
6Q. Given an array of integers, reverse the array by blocks of k.

Examples:

Input: array = [1,2,3,4,5,6], k = 3
Output: [3,2,1,6,5,4]  // Since k is 3, divide the array by a block of 3 elements: [1, 2, 3] and [4,5,6] and reverse it by blocks.

If k doesn't evenly divide, accept and reverse the last block after reversing all of the others.
Input: array = [1,2,3,4,5], k = 3
Output: [3,2,1,5,4] // [1,2,3] and [4,5]

If k exceeds the length of the array, do nothing.
Input: array = [1,2], k = 3
Output: [1,2]
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer array

[input] integer k

[output] array.integer

--------WRONG-----------------------------------------------------------
"""

def solution(array, k):

    if len(array) < k:
        return array
        
    else:
        
        for i in range(0, len(array)//k):
             for j in range(k*i, k*i + k):
                 
                 
                array[k-j-1], array[j] = array[j], array[k-j-1]
                 
            
        return array