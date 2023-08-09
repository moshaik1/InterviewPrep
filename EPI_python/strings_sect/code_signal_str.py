 
"""
 1Q. Given a string, find the character that appears most frequently. You may assume there is only one most frequent character.

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string string

[output] char

"""

# create empty dictionary, iterate through the string and populate the dictionary based on whether char already exists in dict or not
# use max function to get the key with the max value in the dictionary
# .get() used to get the value of each key

def solution(string):
    
    maxFreq = {}
    
    for char in string:
        if char in maxFreq:
            maxFreq[char] += 1
        else:
            maxFreq[char] = 1
            
    maxChar = max(maxFreq, key = maxFreq.get)
    
    
    return maxChar
        




"""
----------------------------------------------------------------
 2Q. Given a string, capitalize the letters at odd positions. The first position of the letter in a string is 1.

Example:
Input: form ation
output: FoRm AtIoN

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string string

[output] string
"""
def solution(string):

    result = []
    
    for i in range(len(string)):
        
        
        
        if i % 2 == 0:
            result.append(string[i].upper())
        else:
            result.append(string[i].lower())
            
    
    return ''.join(result)
    
    


"""
----------------------------------------------------------------
3Q. Given two sentences, merge them into one by alternating words separated by a space. Start with a word from the first sentence.

Example:
Inputs: string1: "Happy Birthday", string2: ""Look! I am flying!"
Output: "Happy Look! Birthday I am flying!"

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string string1

[input] string string2

[output] string


"""

# def solutionP(string1, string2):

#     newArr = []
#     arr1 = [string1.split()]
#     arr2 = [string2.split()]

    
    
    
#     pointer1 = 0
#     pointer2 = 0
    
#     while pointer1 < len(arr1) and pointer2 < len(arr2):
#         newArr.append(arr1[pointer1])
#         pointer1 += 1
#         newArr.append(arr1[pointer2])
#         pointer2 += 1
    
#     if pointer1 < len(arr1):
#         newArr.append(arr1[pointer1:])
        
#     if pointer2 < len(arr2):
#         newArr.append(arr2[pointer2:])
        
    
#     newStr = ' '.join(newArr)
#     return newStr

# print(solutionP("I Like Pie","I Like Candy"))

"""
----------------------------------------------------------------
4Q. Given a string, remove any extra spaces between words (or other non-space characters), keeping only one. You must also remove any trailing or leading spaces so that the first and last character in the resulting string is not a space.

Example:
Input: " Hello World! "
Output: "Hello World!"
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string string

[output] string
"""
def solutionS(string):

    # string to arr
    arr = [string.split()]
    # arr back to string
    newStr = ' '.join(arr)
    res = newStr.strip()
    
    return res

print(solutionS("    Hello     World!            "))



"""
----------------------------------------------------------------
5Q. Given a sentence, find the first occurring longest word excluding punctuation marks (e.g. , . ! ?).

Example:
Input: "Look! I am flying"
Output: "flying"

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string string

[output] string

"""
#def solution(string):



"""
----------------------------------------------------------------
6Q. Given a string, remove all future occurrences of a character after the first occurrence. However, it should preserve all spaces.

Example:

Input: "I am happy"
Output: "I am hpy"
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string string

[output] string


"""
#def solution(string):