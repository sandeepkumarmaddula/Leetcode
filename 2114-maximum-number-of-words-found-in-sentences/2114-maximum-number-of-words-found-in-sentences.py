class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        tol=0
        for i in sentences:
            a=i.split()
            if len(a)>tol:
                tol=len(a)
        return tol