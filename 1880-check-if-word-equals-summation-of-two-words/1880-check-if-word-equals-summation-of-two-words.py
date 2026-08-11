class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        c=''
        d=''
        e=''
        for i in firstWord:
            c+=str(ord(i)-97)
        for i in secondWord:
            d+=str(ord(i)-97)
        for i in targetWord:
            e+=str(ord(i)-97)
        if int(c)+int(d)==int(e):
            return(True) 
        return(False)