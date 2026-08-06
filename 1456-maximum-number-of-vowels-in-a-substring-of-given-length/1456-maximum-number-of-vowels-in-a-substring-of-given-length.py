class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        t=0
        a="aeiouAEIOU"
        for i in range(k):
            if s[i] in a:
                t+=1
        maxx=t
        for i in range(k,len(s)):
            if s[i] in a:
                t+=1
            if s[i-k] in a:
                t-=1
            maxx=max(maxx,t)
        return maxx