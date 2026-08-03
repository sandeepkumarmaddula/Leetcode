class Solution:
    def getSum(self, a: int, b: int) -> int:
        maxn=0xFFFFFFFF
        max=0x7FFFFFFF
        while b:
            carry=(a&b)&maxn
            a=(a^b)&maxn
            b=(carry<<1)&maxn
        return a if a<=max else ~(a^maxn)