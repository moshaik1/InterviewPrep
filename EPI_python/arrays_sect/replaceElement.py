

"""
[ 17 , 18 , 5 , 4 , 6 , 1 ] max = 18
  ^                     ^    
[ 18 , 18 , 5 , 4 , 6 , 1 ] max = 6
       ^                ^    

"""





# 0(n) time
# 0(1) space
# def replaceElements(self, arr: List[int]) -> List[int]:

# # [ 17 , 18 , 5 , 4 , 6 , 1 ]
# #   ^ 
#     if not arr:
#         return []

#     elif len(arr) == 1:
#         return [-1]

#     else:
        
#         i = 0
#         maxNum = arr[i]


#         while i<len(arr)-1:

#             if arr[i] == maxNum:
#                 maxNum = max(arr[i+1:len(arr)])
#                 arr[i] = maxNum
#                 i += 1
                
#             else:
#                 arr[i] = maxNum
#                 i += 1
                    
        
#         arr[len(arr)-1] = -1
#         return arr


            
def replaceElements(self, arr: List[int]) -> List[int]:

    
    m = -1
    for i in range(len(arr)-1,-1,-1):
        newMax = max(m , arr[i])
        arr[i] = m
        m = newMax
        

    return arr

            




