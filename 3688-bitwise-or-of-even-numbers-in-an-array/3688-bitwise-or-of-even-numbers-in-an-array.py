class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        lis=set(nums)
        s=0
        for i in lis:
            if i&1==0:
                s|=i
        return s
