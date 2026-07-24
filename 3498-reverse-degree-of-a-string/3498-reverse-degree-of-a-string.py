class Solution:
    def reverseDegree(self, s: str) -> int:
        ans=0
        idd=1
        for i in s:
            ans+=(123-ord(i))*idd
            idd+=1
        return ans