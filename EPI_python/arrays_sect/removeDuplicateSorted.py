
"""
E: 
- sorted in increasing order!
- returning list of same length, but removed duplicates
B
 [ 1 , 2 , 2 , 3 , 3 , 3 , 6 ]
  i-1  ij
 
     
P
I
V


"""

def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        print(nums)
        return j
    
        