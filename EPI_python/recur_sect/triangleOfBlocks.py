
'''
❓ PROMPT
We have a triangle made of blocks. The topmost row has 1 block, the next row down has 2 blocks, the next row has 3 blocks, and so on. 
Compute recursively (no loops or multiplication) the total number of blocks in such a triangle with the given number of rows.

Example(s)
triangle(2) == 3
triangle(3) == 6
triangle(5) == 15
 

🔎 EXPLORE
List your assumptions & discoveries:
- triangle with 0 rows -> 0
- trianlge cant have negative rows 
- 

Insightful & revealing test cases:
- 0 rows
- even rows
- odd rows

🧠 BRAINSTORM
What approaches could work?
Algorithm 1: 
Time: O(n)
Space: O(n)
 

📆 PLAN
Outline of algorithm #: 
- base case: triagle(1) = 1

# -> 1 
# # -> 3
# # # -> 6
# # # # -> 10
# # # # # -> 15


🛠️ IMPLEMENT
function triangle(rows) {
def triangle(rows: int) -> int:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
def triangle(rows: int) -> int:

    if rows <= 0:
        return 0
    
    return  triangle(rows-1) + rows



print(triangle(12) == 78)
print(triangle(7) == 28)
print(triangle(6) == 21)
print(triangle(5) == 15)
print(triangle(4) == 10)
print(triangle(3) == 6)
print(triangle(2) == 3)
print(triangle(1) == 1)
print(triangle(0) == 0)









