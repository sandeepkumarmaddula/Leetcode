class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        lis=sorted(nums)
        l=len(nums)//2
        i=0
        for _ in range(l):
            lis[i],lis[i+1]=lis[i+1],lis[i]
            i=i+2
        return lis

        