class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums = sorted(set(nums))
        full_series = k * (k + 1) // 2
        for n in nums:
            if n <= k:
                full_series += k - n + 1
                k += 1
            else:
                break
        return full_series