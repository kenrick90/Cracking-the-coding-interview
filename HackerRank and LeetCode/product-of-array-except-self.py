#https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroexist = False
        product=0
        zerocount =0
        for num in nums:
            if num != 0:
                if product == 0:
                    product = num
                else:
                    product *= num
            if num ==0:
                zeroexist = True
                zerocount +=1
            
        answer = [ 0 for _ in range(len(nums))]
        
        i = 0
        if zeroexist == False:
            for num in nums:
                answer[i]  = int(product / num)
                i += 1
                
        elif zeroexist == True and zerocount==1:
            for num in nums:
                if num != 0:
                    answer[i] = 0
                else:
                    answer[i] = product
                i += 1

        
        return answer
        
