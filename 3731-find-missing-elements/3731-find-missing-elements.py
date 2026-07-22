class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mn=min(nums)
        mx=max(nums)
        s=set(nums)
        lis=[]
        for i in range(mn,mx+1):
            if i not in s:
                lis.append(i)
        return lis
    
