#https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/

class Solution:
    def binarySearch(self, nums:List[int], target:int, left:int, right:int):
        
        if left == right and nums[left]==target:
            return left
        
        while left<right:
            mid = (left+right)//2
            if nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            elif nums[mid] == target:
                return mid
            if target > nums[mid]:
                left = mid+1
            else:
                right = mid-1
        return -1
        

    def search(self, nums: List[int], target: int) -> int:
        if nums == None or len(nums) == 0:
            return -1
        if len(nums) == 1 and nums[0] == target:
            return 0
        elif len(nums) == 1 and nums[0] != target:
            return -1
        if sorted(nums) == nums:
            return self.binarySearch(nums,target,0,len(nums)-1)
        
        left,right=0,len(nums)-1
        
        while left<right:
            midpoint = (left + right) //2
            if nums[midpoint] > nums[right]:
                left = midpoint + 1
            else:
                right = midpoint
                
        midpoint = (left + right) //2
        if target >= nums[0]:
            return self.binarySearch(nums,target,0,midpoint-1)
        else:
            return self.binarySearch(nums,target,midpoint,len(nums)-1)
        