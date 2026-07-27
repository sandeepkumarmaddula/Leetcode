class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        s=sorted(nums)
        d={}
        for i,x in enumerate(s):
            if x not in d:
                d[x]=i
        lis=[]
        for i in nums:
            lis.append(d[i])
        return lis 