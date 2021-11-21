
from collections import defaultdict
 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(lambda: 0)
        
        for number in nums:
            hashmap[number] += 1
        
        countmap = [None]* 10000
        
        for key , value in hashmap.items():
            if countmap[value] == None:
                countmap[value] = [key]
            else:
                countmap[value] = countmap[value] + [key]
        # print(countmap)        
        answer = []
        
        for value in range(9999,-1,-1):
            if countmap[value] != None :
                answer = answer + countmap[value]
                k-= len(countmap[value])
            if k == 0:
                break
        return answer
                
                
