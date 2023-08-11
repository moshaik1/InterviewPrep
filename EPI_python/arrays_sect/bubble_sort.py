
'''
🔎 EXPLORE
What are some other insightful & revealing test cases?
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()
 

📆 PLAN
Outline of algorithm #: 


- WITH BUBBLE SORT YOU ARE CONSTANTLY SWAPPING TO GET THE LARGEST ON THE RIGHT
- WITH SELECTION SORT YOU ONLY SWAP WHEN YOU FIND/SELECT THE SMALLEST VALUE, AND SWAP ONCE PER OUTTER LOOP ITERATION
-   outer loop with condition that it goes to end of array
-   inner loop that is charge of swapping
-   compare the current element with the element to the right. If larger than element to right, swap; else, you move pointer over
 
[ 4 , 9 , 1 , 10 , 2 , 6 , 7 ]  i = 0   j[0] = 4  j[0+1] = 9
  ^   ^
[ 4 , 9 , 1 , 10 , 2 , 6 , 7 ]  i = 0   j[1] = 9  j[1+1] = 1     swap 
      ^   ^
[ 4 , 1 , 9 , 10 , 2 , 6 , 7 ]  i = 0   j[2] = 9  j[2+1] = 10     
          ^   ^
[ 4 , 1 , 9 , 10 , 2 , 6 , 7 ]  i = 0   j[3] = 10  j[3+1] = 2     swap 
               ^   ^
[ 4 , 1 , 9 , 2 , 10 , 6 , 7 ]  i = 0   j[4] = 10  j[4+1] = 6     swap 
                   ^   ^
[ 4 , 1 , 9 , 2 , 6 , 10 , 7 ]  i = 0   j[5] = 10  j[4+1] = 7     swap 
                       ^   ^
[ 4 , 1 , 9 , 2 , 6 , 7 , 10 ]  i = 0   j[6] = 10  j[4+1] = 7     swap 
                       ^   ^
 
      

🛠️ IMPLEMENT
Write your algorithm.
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

def bubbleSort( input: list[int]) -> list[int]:

    for i in range(0, len(input)):
        j = 1
        while j < len(input)-i:
            
            # swap
            if input[j-1] > input[j]:
                input[j-1], input[j] = input[j], input[j-1]
                j += 1
            else:
                j += 1
    
    return input


print(bubbleSort([5,4,3,2,1]))
print(bubbleSort([]))
print(bubbleSort([5,4,3,2,1,1]))
print(bubbleSort([5,5,4,3,2,1]))
print(bubbleSort([5,4]))

   


        