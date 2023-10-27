
"""
Given an integer array nums, 
rotate the array to the right by k steps, where k is non-negative.

E:
assumptions->   
    array length greater than 1 
    k is 0 or positive

    [ 10 , 2 , 5 , 1 , 15 , 9] k = 3 -> [ 1 , 15 , 9 , 10 , 2 , 5 ]

    [ 10 , 2 , 5 , 1 , 15 , 9] 
       i

    [ 9 , 2 , 5 , 1 , 15 , 9]
    temp = 10
        save current i to temp
        arr[i] = arr[last digit]




    
B
P
I
V


"""

def rotate(nums, k):
    """
    [ 10 , 2 , 5 , 1 , 15 , 9 , 6 ]  k = 3 ->  [ 15 , 9 , 6, 10 , 2 , 5 , 1 ]
       
    Do not return anything, modify nums in-place instead.
    """
   
    if k == 0 or k >= len(nums):
        return nums
    else:
        L = 0
        
        
        while k > 0:
            temp = nums[L]
            nums[L] = nums[len(nums) - k]
            L += 1
            k -= 1
            
            while L < len(nums) - k:
                nums[L], temp = temp, nums[L]
                L += 1
        return nums
    

print(rotate([10 , 2 , 5 , 1 , 15 , 9 , 6] , 2))