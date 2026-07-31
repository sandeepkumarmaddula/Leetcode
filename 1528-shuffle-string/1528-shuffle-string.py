class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        d=dict(zip(indices,s))
        lis=sorted(indices)
        s=""
        for i in lis:
            s+=d[i]
        return s
