class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a=1
        b=0
        while n>0:
            d=n%10
            a*=d
            b+=d
            n//=10
        return a-b