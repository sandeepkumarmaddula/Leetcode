class Solution:
    def tribonacci(self, n: int) -> int:
        if n<=1: return n
        lis=[0,1,1]
        for i in range(2,n): lis.append(lis[-1]+lis[-2]+lis[-3])
        return lis[-1]