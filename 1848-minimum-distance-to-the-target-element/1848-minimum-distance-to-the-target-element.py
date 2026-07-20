class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        re=len(nums)
        for i in range(len(nums)):
            if nums[i]==target:
                re=min(re,abs(i - start))
        return re
