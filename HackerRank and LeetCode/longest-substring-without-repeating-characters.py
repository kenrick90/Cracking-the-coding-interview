#https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        wstart = 0
        maxlen = 0
        charexistmap = {}
        for wend in range(length):
            if s[wend] in charexistmap.keys():
                charexistmap[s[wend]] +=1
            else:
                charexistmap[s[wend]] =1
            
            while charexistmap[s[wend]] > 1:
                charexistmap[s[wstart]] -=1
                wstart +=1
                
            maxlen=max(maxlen,wend-wstart+1)
        return maxlen
        
        
