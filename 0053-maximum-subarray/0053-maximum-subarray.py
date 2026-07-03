class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        con=nums[0]
        max_sub=nums[0]
        for i in range(1,len(nums)):
            con=max(nums[i],con+nums[i])
            max_sub=max(max_sub,con)
        return max_sub