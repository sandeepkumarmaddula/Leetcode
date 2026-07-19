class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s=set(allowed)
        tol=0
        for i in words:
            if all(j in s for j in i):
                tol+=1
        return tol