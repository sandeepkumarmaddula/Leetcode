class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        a=len(set(candyType))
        b=len(candyType)/2
        return int(a) if int(b)>int(a) else int(b)