class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        lis=[0,1]
        for i in range(2,n+1):
            lis.append(lis[-1]+lis[-2])
        return lis[-1]