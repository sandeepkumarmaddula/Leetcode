class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        c=''
        d=set()
        for i in word:
            if i.isdigit():
                c+=i
            else:
                if c:
                    d.add(c.lstrip('0') or '0')
                    c=''
        if c:
            d.add(c.lstrip('0') or '0')
        return len(d)