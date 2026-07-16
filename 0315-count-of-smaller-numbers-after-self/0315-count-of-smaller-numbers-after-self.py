class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        lis=[]
        ss=sorted(nums)
        for i in nums:
            a=bisect_left(ss,i)
            lis.append(a)
            del ss[a]
        return lis