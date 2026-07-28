class Solution:
    def maxScore(self, s: str) -> int:
        max_score=zeros= 0
        ones=s.count('1')
        for i in range(len(s) - 1):
            zeros+=s[i]=='0'
            ones-=s[i]=='1'
            max_score = max(max_score,zeros+ones)
        return max_score