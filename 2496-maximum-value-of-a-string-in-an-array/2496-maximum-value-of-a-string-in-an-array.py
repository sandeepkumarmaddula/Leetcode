class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        max_len=float("-inf")
        for i in strs:
            if i.isdigit():
                if max_len<int(i):
                    max_len=int(i)
            else:
                if max_len<len(i):
                    max_len=len(i)
        return max_len