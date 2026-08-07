class Solution:
    def sortSentence(self, s: str) -> str:
        s=s.split()
        c=[""] * len(s)
        for i in s:
            d=int(i[-1])-1
            c[d]=i[:-1]
        return ' '.join(c)