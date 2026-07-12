class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ar=sorted(set(arr))
        d={}
        i=1
        for num in ar:
            d[num]=i
            i+=1
        tol=[]
        for i in arr:
            tol.append(d[i])
        return tol