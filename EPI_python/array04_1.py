
# parity of binary word is 1 if number of 1s in the word is odd, else it is 0
# parity(1011) -> 1
# parity(10001000) -> 0
# how to get parity of a very large number of 64bit words?

# Brute Force: we only care if number of 1s is even or odd, so track number of 1s so far (accummorator pattern)
# Time: O(n)
# Space: O(1)

# have a accumulator variable that keeps track of 1s and a pointer 
# if 
#
#
#


def parity(x: int)->int:
    result = 0
    while x:
        print("x= ", x)
        print("result= ", result)
        print("x & 1 = ", x&1 )
        result = result ^ x & 1
        x = x >> 1
    return result





print(parity(12))   
# 0000 1100 => 12   x=>12 x&1=>0  result=0  new result=>0
# 0000 110 => 6     x=>6 x&1=>0  result=0  new result=>0
# 0000 11 => 3      x=>3 x&1=>1  result=0  new result=>1
# 0000 1 => 1      x=>1 x&1=>1  result=1  ANSWER=>0
