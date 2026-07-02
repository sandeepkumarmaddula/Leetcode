class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        s=""
        l=[]
        for i in nums:
            s+=str(i)
        for i in s:
            l.append(int(i))
        return l