class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mi=min(nums)
        mx=max(nums)
        lis=[]
        for i in range(1,mx+1):
            if mi%i==0 and mx%i==0:
                lis.append(i)
        return max(lis)