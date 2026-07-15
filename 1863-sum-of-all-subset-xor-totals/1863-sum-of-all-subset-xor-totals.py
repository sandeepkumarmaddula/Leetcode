class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        x=0
        for i in nums:
            x|=i
        n=len(nums)
        return x*(2**(n-1))