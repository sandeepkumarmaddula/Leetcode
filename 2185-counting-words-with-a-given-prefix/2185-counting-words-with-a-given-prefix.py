class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        t=0
        for i in words:
            if pref==i[:len(pref)]:
                t+=1
        return t