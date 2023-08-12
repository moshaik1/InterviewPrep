"""
1Q. Given an array of integers, move all negative numbers to the left in the order they appear.

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer array

unsorted array

[output] array.integer

sorted array

--------CORRECT-----------------------------------------------------------
"""
# def solution(array):
#     answer = []
#     for i in range(0, len(array)):
#         if array[i] < 0:
#             answer.append(array[i])
        
#     for j in range(0, len(array)):
#         if array[j] > 0:
#             answer.append(array[j])
            
            
            
#     return answer
        

"""
2Q. Given a sorted array of integers and a target integer, check if the array contains a target using binary search.

The array may contain duplicate values.
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer array

[input] integer target

target value to be checked

[output] boolean

--------WRONG---CHECKED--------------------------------------------------------
"""

# def solution(array, target):

#     tail = len(array) - 1
#     head = 0

#     while head <= tail:
#         midpoint = (tail + head) // 2

        

#         if array[midpoint] == target:
#             return midpoint
#         elif array[midpoint] < target:
#             head = midpoint+1
#         else:
#             tail = midpoint-1
#     return -1

# print(solution([],12))
# print(solution([10,12],12))
# print(solution([10,13,15,16,20],12))
# print(solution([10,12,13,16],13))
# print(solution([10,13,15,16,20],16))
    

    
"""
3Q. Given an array of integers, move all odd numbers to the left in the order they appear.

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer array

unsorted array

[output] array.integer

sorted array
--------CORRECT-----------------------------------------------------------
"""

# def solution(array):
    
#     result = []
    
#     for i in range(len(array)):
#         if array[i] % 2 == 1:
#             result.append(array[i])
            
    
#     for j in range(len(array)):
#         if array[j] % 2 == 0:
#             result.append(array[j])


#     return result

"""
4Q. Given three sorted array of integers, merge them into a single sorted list.

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer array1

[input] array.integer array2

[input] array.integer array3

[output] array.integer

sorted list
--------WRONG-----------------------------------------------------------
"""
# def solution(array1, array2, array3):
    
#     answer = []
#     totLength = len(array1) + len(array2) + len(array3)
    
#     pointer1 = 0
#     pointer2 = 0
#     pointer3 = 0
#     respointer = 0
        
    
#     while respointer < totLength:
        
#         if array1[pointer1] <= array2[pointer2] and array1[pointer1] <= array3[pointer3]:
#             answer.append(array1[pointer1])
#             pointer1 += 1
#             respointer +=1
        
#         elif array2[pointer2] <= array1[pointer1] and array2[pointer2] <= array3[pointer3]:
#             answer.append(array2[pointer2])
#             pointer2 += 1
#             respointer +=1
            
#         else:
#             answer.append(array3[pointer3])
#             pointer3 += 1
#             respointer +=1
    
#     return answer

"""
5Q. Given two array of integers of equal length, zip them up by alternating between the two arrays.

Ex. [1, 2], [3, 4] returns [1, 3, 2, 4]

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer array1

[input] array.integer array2

[output] array.integer
--------CORRECT-----------------------------------------------------------
"""

# def solution(array1, array2):
    
#     answer = []
#     pointer2 = 0
    
#     for i in range(len(array1)):
#         answer.append(array1[i])
#         answer.append(array2[pointer2])
#         pointer2 += 1
        
#     return answer

"""
6Q. Given a sorted array and a target value, return the value that is closest to the target value. If two values are equally close to the target, return the smaller one. If no such value exists, return -1.

Ex. [1, 3, 5, 7], target: 6 returns 5

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer array1

[input] integer target

[output] integer

--------WRONG-----------------------------------------------------------
"""
# def solution(array1, target):

#     if is not target or is not array1:
#         return -1
        
#     else:
#         answer = 0
#         for i in range(len(array1)-1):
            
#             if target - array1[answer] < target - 
            
          
            
            
