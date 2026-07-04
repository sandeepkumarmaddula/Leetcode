class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        list1=[]
        for i in nums1:
            s=nums2.index(i)
            for j in nums2[s:]:
                if j>i:
                    list1.append(j)
                    break
            else:
                list1.append(-1)
        return list1