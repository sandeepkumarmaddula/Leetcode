class Solution:
    def secondHighest(self, s: str) -> int:
        a=sorted(set(i for i in s if i.isdigit()))
        if len(a)<2: return -1
        else: return int(a[-2])