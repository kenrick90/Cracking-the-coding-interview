# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 103
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        numMap = {}
        index=0
        for number in nums:
        	if number in numMap:
        		newlist = numMap[number]
        		newlist.append(index)
        		numMap[number] = newlist
        	else :
        		numMap[number] = [index]
        	index +=1

        half = int(target/2)

        if target % 2 == 0 and half in numMap.keys():
        	if len(numMap[half]) > 1:
        		return numMap[half]

        for key in numMap.keys():
        	if (target - key) in numMap and (target - key) != key:
        		output.append(numMap[key][0])
        		output.append(numMap[target-key][0])
        		return output
        

if __name__ == "__main__":
	solution = Solution()
	assert solution.twoSum([2,7,11,15], 9) == [0,1] ,"wrong"
	assert solution.twoSum([3,2,4], 6) == [1,2] ,"wrong"
