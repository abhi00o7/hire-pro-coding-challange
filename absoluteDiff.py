'''
Given a number N. The task is to return all the numbers less than or equal to N in increasing order, with the fact that absolute difference between any adjacent digits of number should be 1.
Input: N = 20
Output: 10 12
Explanation: Diff between 1 and 0 and
Diff between 1 and 2 is one.
'''

from bigO import BigO
from bigO import algorithm

def absDifOne( N):
    # code here
    digits = []
    for i in range (N+1):
        arr = list(map(int,str(i)))
        diff = 0
        diffArr = []
    # print(arr)
        for j in range(len(arr)-1):

            diff = abs(arr[j] - arr[j+1])
            diffArr.append(diff)
        diffSet = list(set(diffArr))
    # print(diffSet)
        if(len(diffSet) == 1 and diffArr[0] == 1):
            digits.append(i)

    return digits

print(absDifOne(20))


lib = BigO()

# lib.test(absDifOne(100),"random")
complexity = lib.test(absDifOne, "random")
complexity = lib.test(absDifOne, "sorted")
complexity = lib.test(absDifOne, "reversed")
complexity = lib.test(absDifOne, "partial")
complexity = lib.test(absDifOne, "Ksorted")