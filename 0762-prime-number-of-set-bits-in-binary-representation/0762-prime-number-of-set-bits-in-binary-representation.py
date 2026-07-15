class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        lis=[2,3,5,7,11,13,17,19,23]
        cou=0
        for i in range(left,right+1):
            a=bin(i).count('1')
            if a in lis:
                cou+=1
        return cou