class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        number, length, vlen = 0, len(intervals), len(intervals)
        if length>1:
            right=intervals[0][1]
        else:
            return 0
        
        for i in range(1,length):
            if right > intervals[i][0]:
                number+=1
            else:
                right = intervals[i][1]
                
        return number
        
        
        
