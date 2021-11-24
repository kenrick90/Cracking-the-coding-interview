https://leetcode.com/problems/gas-station/
  
  class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
#                 0 1 2 3 4 
#         gas     1 2 3 4 5
#         cost    3 4 5 1 2
        
        numOfStation = len(gas)
        for i in range(numOfStation):
            remainderfuel = gas[i] - cost[i]
            j = i
            count = 0
            while remainderfuel >= 0 and count < numOfStation:       
                j += 1
                j = j % numOfStation
                remainderfuel = remainderfuel + gas[j] - cost[j]
                count += 1
            if count == numOfStation and remainderfuel >= 0:
                return i
        return -1
