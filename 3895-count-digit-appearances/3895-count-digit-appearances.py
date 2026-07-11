class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        tol=0
        s=""
        for i in nums:
            s+=str(i)
        for i in s:
            if int(i)==digit:
                tol+=1
        return tol