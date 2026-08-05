class Solution:
    def maxPower(self, s: str) -> int:
        eli=s[0]
        cou=1
        lis=[]
        for i in range(1,len(s)):
            if eli==s[i]: cou+=1
            else:
                lis.append(cou)
                cou=1
            eli=s[i]
        lis.append(cou)
        return max(lis)   