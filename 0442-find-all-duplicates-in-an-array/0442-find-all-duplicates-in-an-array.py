class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        a=[]
        s=set()
        for i in nums:
            if i not in s:
                s.add(i)
            else:
                a.append(i)
        return a