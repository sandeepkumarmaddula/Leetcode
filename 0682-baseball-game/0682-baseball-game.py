class Solution:
    def calPoints(self, operations: List[str]) -> int:
        list1=operations
        lis=[]
        for i in operations:
            if i=="+": lis.append(lis[-2]+lis[-1])
            elif i=="D": lis.append(lis[-1]*2)
            elif i=="C": lis.pop()
            else: lis.append(int(i))
        return sum(lis)
