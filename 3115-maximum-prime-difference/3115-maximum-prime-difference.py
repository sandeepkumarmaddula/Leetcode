class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        lis=[]
        for i,x in enumerate(nums):
            if x>=2:
                for j in range(2,int(x**0.5)+1):
                    if nums[i]%j==0: break
                else: lis.append(i)
        if len(lis)<=1: return 0
        else: return lis[-1]-lis[0]

