class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxx=float("-inf")
        low=0
        for i in nums:
            if i==1:
                low+=1
            else:
                maxx=max(maxx,low)
                low=0
        return max(maxx,low)
