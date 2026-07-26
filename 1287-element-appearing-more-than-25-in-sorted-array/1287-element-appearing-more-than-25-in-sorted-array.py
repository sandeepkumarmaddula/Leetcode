class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        le=len(arr)//4
        d={}
        l=[]
        for i in arr:
            d[i]=d.get(i,0)+1
        for i in d.keys():
            if d[i]>le:
                l.append(i)
        return max(l)