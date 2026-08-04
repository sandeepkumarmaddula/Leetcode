class Solution:
    def reverseVowels(self, s: str) -> str:
        i=0
        j=len(s)-1
        a="AEIOUaeiou"
        s=list(s)
        while i<j:
            if s[i] in a and s[j] in a:
                s[i],s[j]=s[j],s[i]
                j-=1
                i+=1
            elif s[j] not in a:
                j-=1
            else: i+=1
        return "".join(s)