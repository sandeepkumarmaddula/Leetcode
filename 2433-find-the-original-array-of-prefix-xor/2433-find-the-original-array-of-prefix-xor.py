class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        if len(pref)<=1: return pref
        list1=pref[0]
        list2=[list1]
        for i in range(1,len(pref)):
            s=pref[i]^pref[i-1]
            list2.append(s)
        return list2
