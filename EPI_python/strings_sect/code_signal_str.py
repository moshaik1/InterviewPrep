 
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

# def solution(string):
    
#     maxFreq = {}
    
#     for char in string:
#         if char in maxFreq:
#             maxFreq[char] += 1
#         else:
#             maxFreq[char] = 1
            
#     maxChar = max(maxFreq, key = maxFreq.get)
    
    
#     return maxChar
        




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
# def solution(string):

#     result = []
#     pointer = 0
#     for i in range(len(string)):

#         if string[i] == " ":
#             result.append(string[i])
#             continue
        
#         if pointer % 2 == 0:
#             result.append(string[i].upper())
#             pointer += 1
#         else:
#             result.append(string[i].lower())
#             pointer += 1
            
    
#     return ''.join(result)
    

# print(solution("mohsin shaik"))
# print(solution("mohsinshaik"))
# print(solution("MOHSIN SHAIK"))
    


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

# def solutionP(string1:str, string2:str)-> str:

#     newArr = []
#     arr1 = string1.split()
#     arr2 = string2.split()

    
    
    
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
# def solutionS(string):
# def solutionS(string):

#     # string to arr
#     arr = [string.split()]
#     # arr back to string
#     newStr = ' '.join(arr)
#     res = newStr.strip()
    
#     return res

# print(solutionS("    Hello     World!            "))
#     string = string.strip()
    
#     newStr = ""

    

#     for i in range(0 , len(string)):

#         if string[i] != " ":
#             newStr += string[i]
        
#         else:
#             if string[i] == " " and string[i+1] != " ":
#                 newStr += string[i]
        

#     return newStr

# print(solutionS("    Hello     World!            "))
# print(solutionS("    Hello  Poop   World!            "))
# print(solutionS("    Hello     World!"))


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
def solution(string):
    count = 0
    start = 0
    maxStarting = 0
    flag = False
    i = 0

    while i < len(string):

        
        while flag is False:
            if string[i].isalnum():
                count += 1
                i += 1
            elif string[i].isalnum() is False:
                i += 1
            elif string[i].isspace():
                
            

        
        
                if string[i].isalnum() is False and string[i].isspace() is False:
                    continue




    
def solutionT(string):
    front = 0
    end = 0
    largest = 0
    largestPointer = 0

    while end < len(string):
        if not string[end].isspace():
            end += 1
        else:
            largest = max(largest , len(string[front:end]))
            end += 1
            front = end
    largest = max(largest, len(string[front:end]))

    print(largest)
    

print(solutionT("Look! I am flying"))




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
# def solution7(string):
    
#     answer = ""

#     for i in range(0, len(string)):

#         if string[i] not in string[:i] or string[i] == " ":
#             answer += string[i]

#     return answer


# print(solution7("I am happy"))
# print(solution7("I am ha pp y"))
# print(solution7("bad bad dab topd"))
# print(solution7("I am happy"))