class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        
        if i == 0:
            return
        
        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1
        
        if i == 0:
            nums[i:] = nums[i:][::-1]
            return
        
        j = i
        while (j < len(nums)) and (nums[j] - nums[i-1] > 0):
            j += 1

        temp = nums[i-1]
        nums[i-1] = nums[j-1]
        nums[j-1] = temp
        nums[i:] = nums[i:][::-1]
        
        
        
        
        
        
