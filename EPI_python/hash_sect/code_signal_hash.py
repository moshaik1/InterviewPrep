
"""
1Q Determine whether a ransomNote string can be created from the characters in the magazine string.

Create an empty dictionary to store the frequencies of each character in the magazine.
For each character in magazine
Count the frequency of it
For each character in ransomNote
If it never occurred or there's no remaining frequency of it, return False
Otherwise decrement the frequency of it
Return True as it's possible to create the ransomNote string from the magazine string
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string ransomNote

[input] string magazine

[output] boolean

"""

# def solution(ransomNote, magazine):

#     magazChars = {}
    
#     for char in magazine:
#         if char in magazChars:
#             magazChars[char] += 1
            
#         else:
#             magazChars[char] = 1
            
    
#     for char in ransomNote:
        
#         if magazChars.get(char) == 1:
#             del magazChars[char]
#         elif char not in magazChars:
#             return False
#         else:
#             magazChars[char] -= 1
            
#     return True
            
        
            
        

"""
2Q Initialize a dictionary.
For each element in the input list nums
If target minus n exists in the dictionary return a tuple first containing the index of target - n and then the index of n.
Otherwise, add n to the dictionary as the key with its index in the list as the value
If the loop completes without finding a pair of elements that sum to target, return an empty array.
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer nums

[input] integer target

[output] array.integer



"""
# def solution(nums, target):
    
#     dict = {}
    
#     for n in range(len(nums)):
        
#         if (target-nums[n]) in dict:
#             return ( dict.get(target-nums[n] ), n )
#         else:
#             dict[ nums[n] ] = n
            
#     return []



"""
3Q Create a new empty set
For each element in the input array
If it is in the set, return true because we've seen this element before
Otherwise, add it to the set
After the loop finishes, return false because there were no duplicate values in the input array
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer array

[output] boolean


"""
# def solution(array):

#     empySet = set()

#     for num in array:
#         if num in empySet:
#             return True
#         else:
#             empySet.add(num)
    
#     return False


"""
4Q Create a dictionary to store the frequency of each integer in the array
For each element in the array
Count its frequency
Track the highest frequency seen
For each element in the dictionary
If the frequency is equal to the highest frequency, return the key
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer array

[output] integer
"""
# def solution(array):
    
#     # populate the dictionary with key:number and value:freq
#     freqDict = {}
#     answer = []
#     highestFreq = float("-inf")
#     highestFreqNum = 0

#     for num in array:
#         if num in freqDict:
#             freqDict[num] = freqDict.get(num) + 1
#         else:
#             freqDict[num] = 1
        
#         if freqDict.get(num) > highestFreq:
#             highestFreq = freqDict.get(num)
#             highestFreqNum = num
#     print(highestFreqNum,highestFreq)
#     print(freqDict.items())


#     for key, val in freqDict.items():
#         if val == highestFreq:
#             answer.append(key)
            
        
           
            

    
#     return answer

   


# print(solution([ 1 , 2 , 3 , 1 , 2 , 3 , 3 , 3 , 4 , 2, 2]))
    
    
    



"""
5Q Initialize a dictionary
Iterate through the array, for each element
track the frequency of the value in the array
Iterate through the dictionary, for each element
if any element has a count greater than half the length of the array, return the element
Otherwise return None
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer arr

[output] integer



"""
def solution(arr):
    
    dict = {}
    
    for num in arr:
        if num in dict:
            dict[num] = dict.get(num)+1
        else:
            dict[num] = 1

    for key,val in dict.items():
        if val > (len(arr)//2):
            return key
        else:
            return None
        



print(solution([ 1 , 1 , 2 , 1 , 1 , 1]))
print(solution([ 1 , 2 , 3 , 1 , 2 , 3 , 3 , 3 , 4 , 2, 2]))