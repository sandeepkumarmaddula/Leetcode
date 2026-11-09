class Solution:
    def waysToReachStair(self, k: int) -> int:
        return sum(comb(j + 1, (1 << j) - k) for j in range(40) if 1 << j >= k)
        