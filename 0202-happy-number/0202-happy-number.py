class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1 or n==7: return True
        elif(n<10):
            return False
        else:
            s=0
            while(n>0):
                a=n%10
                s+=a**2
                n=n//10
            return self.isHappy(s)