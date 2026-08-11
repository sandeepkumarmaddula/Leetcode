class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d={}
        for i in s:
            d[i]=d.get(i,0)+1
        for i in range(len(s)):
            if d[s[i]]!=d[s[i-1]]:
                return(False)
        return True