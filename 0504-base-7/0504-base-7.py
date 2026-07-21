class Solution:
    def convertToBase7(self, num: int) -> str:
        if num==0: return "0"
        neg=num<0
        num=abs(num)
        s=""
        while num>0:
            s=str(num%7)+s
            num//=7
        if neg:
            s="-"+s
        return "".join(s)
        