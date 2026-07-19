class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        l=0
        t=0
        for i in range(len(gain)):
            a=gain[i]+t
            t=a
            if t>l:
                l=t
        return l