class Solution:
    def toLowerCase(self, s: str) -> str:
        l=""
        for i in s:
            if i.isupper(): l+=i.lower()
            else: l+=i
        return l