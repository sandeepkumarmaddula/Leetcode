class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        res = []
        maxx = max(nums)
        minn = min(nums)
        for i in range(minn,maxx+1):
            if i not in nums:
                res.append(i)
        return res
    
