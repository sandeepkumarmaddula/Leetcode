class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        fir=sum(nums[:k])
        maxx=fir
        for i in range(k,len(nums)):
            fir+=nums[i]-nums[i-k]
            maxx=max(maxx,fir)
        return maxx/k