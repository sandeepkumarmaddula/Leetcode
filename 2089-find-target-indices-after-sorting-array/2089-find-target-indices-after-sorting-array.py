class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==0:
            return []
        nums.sort()
        lis=[]
        for i in range(len(nums)):
            if nums[i]==target:
                lis.append(i)
            elif nums[i]>target:
                break
        return lis