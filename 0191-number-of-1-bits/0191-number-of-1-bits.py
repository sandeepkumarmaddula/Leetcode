class Solution:
    def hammingWeight(self, n: int) -> int:
        ret=0
        for i in range(32):
            if (n>>i)&1:
                ret+=1
        return ret