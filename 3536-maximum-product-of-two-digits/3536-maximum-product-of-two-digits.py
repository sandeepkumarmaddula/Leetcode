class Solution:
    def maxProduct(self, n: int) -> int:
        lis=list(str(n))
        lis.sort()
        return int(lis[-1])*int(lis[-2])