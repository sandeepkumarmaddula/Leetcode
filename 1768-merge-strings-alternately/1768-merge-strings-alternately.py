class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1=len(word1)
        l2=len(word2)
        i=0
        j=0
        s=""
        while l1>i and l2>j:
            s+=word1[i]+word2[j]
            i+=1
            j+=1
        while l1>i:
            s+=word1[i]
            i+=1
        while l2>j:
            s+=word2[j]
            j+=1
        return s