class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        a=n*2
        if n%2==0 and a>n:
            return n
        else: return a