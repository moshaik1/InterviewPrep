# The Dutch National Flag Problem 

# program that takes array A and an index in A, and rearrange such that all elements less than A[i] (pivot) appear first, elements equal to pivot appear next, and
# elements greater than A[i] appear last

# ex. [ 4 , 2 , 6 , 1 , 9 , 8 , 5]  pivot = 3 =>  [ 2 , 4 , 6 , 1 , 5 , 8 , 9]
# ex. [ 0 , 0 , 1 , 1 , 1 , 2 , 2]  pivot = 1   pivotVal = 1  =>  [ ]
#               i^          T^                




def dutchNationalFlagProblem(arr:list[int], pivot:int ) -> list[int]:
    pivotVal = arr[pivot]

    temp = 0

# elements less than pivot val. 
    for i in range(0, len(arr)):
        if arr[i] < pivotVal:
            arr[temp],arr[i] = arr[i], arr[temp]
            temp += 1

# elements greater than pivot val
    temp = len(arr) - 1

    for i in range(len(arr)-1, -1 , -1):
        if arr[i] > pivotVal:
            arr[temp],arr[i] = arr[i],arr[temp]
            temp -= 1
        if arr[i] < pivotVal:
            return arr

    return arr


print(dutchNationalFlagProblem([0,1,2,0,2,1,1], 1))
 
