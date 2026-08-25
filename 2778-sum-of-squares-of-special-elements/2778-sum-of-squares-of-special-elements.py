class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        tol=0
        for i in range(len(nums)):
            if len(nums)%(i+1)==0:
                a=nums[i]*nums[i]
                tol+=a
        return tol