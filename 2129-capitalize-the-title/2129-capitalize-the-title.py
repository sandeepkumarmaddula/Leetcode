class Solution:
    def capitalizeTitle(self, title: str) -> str:
        x=list(title.lower().title().split())
        for i in range(len(x)):
            if len(x[i])<=2: 
                x[i]=x[i].lower()
        return " ".join(x)
