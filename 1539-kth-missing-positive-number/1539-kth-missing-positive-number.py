class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        t=0
        i=1
        while i>0:
            if i not in arr:
                t+=1
                if t==k:
                    return i
                else: i+=1
            else: i+=1
            