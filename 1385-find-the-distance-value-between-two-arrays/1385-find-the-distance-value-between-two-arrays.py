class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        res=0
        for i in arr1:
            t=False
            for j in arr2:
                if abs(i-j)<=d:
                    t=True
                    break
            if not t:
                res+=1
        return res
            
                