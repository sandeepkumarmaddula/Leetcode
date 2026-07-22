class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            num=list(str(n))
            mul=1
            for i in range(len(num)):
                mul*=int(num[i])
            if mul%t==0:
                return n
            else:
                n=n+1
        return n