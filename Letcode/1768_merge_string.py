
"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
 

Constraints:

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.

EXPLORE
    - if 1 sting is empty, can I return the other string
    - if both strings are empty, do I return an empty string

    useful test cases:
    - word1 longer than word2
    - word2 longer than word1
    - word1 and word2 same length
    - word1 is empty
    - word2 is empty
    - both are empty

BRAINSTORM

PLAN
IMPLEMENT 
VERIFY



"""


def merge_strings(str1: str , str2: str) -> str:
    length1 = len(str1)
    length2 = len(str2)
    
    answer = ""

    if str1 is None or str2 is None:
        return ""
    
    i = 0
    j = 0
    answerpt = 0

    if length1 > length2:
        while j < length2:
            
            answer[answerpt] += str1[i]
            answerpt += 1
            i+=1
            answer[answerpt] += str2[j]
            answerpt += 1
            j+=1
        answer[answerpt] += str1[i:]

    if length1 < length2:
        while i < length1:
            answer[answerpt] += str1[i]
            answerpt += 1 
            i+=1
            answer[answerpt] += str2[j]
            answerpt += 1
            j+=1
        answer[answerpt] += str2[j:]


    if length1 == length2:
        while i < length1:
            answer[answerpt] += str1[i]
            answerpt += 1 
            i+=1
            answer[answerpt] += str2[j]
            answerpt += 1
            j+=1
    
    return answer



print(merge_strings("dog","cat"))