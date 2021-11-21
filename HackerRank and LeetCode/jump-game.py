class Solution:
    def canJump(self, nums: List[int]) -> bool:
        distance = len(nums)
        if distance ==1:
            return True
        
        furthest = nums[0]
        i=0
        
        while i <= furthest and i < distance:
            furthest = max(i + nums[i],furthest)
            i+=1
            if furthest >= distance-1:
                return True
        return False
        
