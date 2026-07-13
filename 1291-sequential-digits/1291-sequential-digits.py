class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s="123456789"
        lis=[]
        i=0
        leng=len(str(low))
        while leng<=len(str(high)):
            if i+leng>9:
                leng+=1
                i=0
                continue
            num=int(s[i:i+leng])
            if num > high:
                break
            if num>=low:
                lis.append(num)
            i+=1
        return lis
