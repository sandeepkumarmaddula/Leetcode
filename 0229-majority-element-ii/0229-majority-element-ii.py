class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d={}
        a=[]
        l=len(nums)/3
        for i in nums:
            d[i]=d.get(i,0)+1
        for i in d.keys():
            if d[i]>l:
                a.append(i)
        return a