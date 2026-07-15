class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        s=[]
        a=max(candies)
        for i in candies:
            s.append((i+extraCandies)>=a)
        return s