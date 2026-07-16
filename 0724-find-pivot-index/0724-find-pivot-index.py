class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        tol=sum(nums)
        l=0
        for i in range(len(nums)):
            right=(tol-l-nums[i])
            if l==right:
                return i
            l+=nums[i]
        else:
            return -1