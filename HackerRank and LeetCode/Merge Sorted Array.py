#https://leetcode.com/problems/merge-sorted-array/submissions/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        if n == 0:
            return
        i = 0
        numA = len(nums1)
        nums1[-n:] = [ None for _ in range(n)]
        
        
        
        for element in nums2:
            while i < numA:
                if nums1[i] is None:
                    nums1[i] = element
                    i += 1
                    break
                elif element < nums1[i]:
                    nums1[i+1:] = nums1[i:-1] 
                    nums1[i] = element
                    i +=1
                    break
                else:
                    i += 1

