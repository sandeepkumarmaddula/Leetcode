class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s=str(n)
        con=0
        for i in range(0,len(s)):
            if i&1==0:
                con+=int(s[i])
            else:
                con-=int(s[i])
        return con