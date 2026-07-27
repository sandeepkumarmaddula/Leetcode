class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        lis=[]
        for i in range(len(nums)):
            if nums[i]<2: continue
            t=True
            for j in range(2,int(nums[i]**0.5)+1):
                if nums[i]%j==0:
                    t=False
                    break
            if t:
                lis.append(i)
        if len(lis)<=1:
            return 0
        else:
            return lis[-1]-lis[0]

