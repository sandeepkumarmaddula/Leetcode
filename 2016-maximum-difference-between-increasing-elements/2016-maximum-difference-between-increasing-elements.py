class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        l=-1
        n=nums[0]
        for i in range(1,len(nums)):
            if nums[i] > n: l=max(l,nums[i]-n)
            else: n=nums[i]
        return l