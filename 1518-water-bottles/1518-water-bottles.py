class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        c=0
        num=numBottles
        while numBottles>=numExchange:
            a=numBottles//numExchange
            c+=a
            b=numBottles%numExchange
            numBottles=a+b
        return c+num