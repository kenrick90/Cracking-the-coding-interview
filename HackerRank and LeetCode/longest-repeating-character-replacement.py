#https://leetcode.com/problems/longest-repeating-character-replacement/
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length=len(s)
        maxlen = 0
        wstart=0
        characters = [0]*26
        maxcount=0
        for wend in range(length):
            characters[ord(s[wend])-ord('A')] +=1
            currentcharactercount = characters[ord(s[wend])-ord('A')]
            maxcount = max(maxcount,currentcharactercount)
            
            while(wend - wstart-maxcount +1 > k):
                characters[ord(s[wstart]) - ord('A')] -=1
                wstart +=1
            maxlen = max (maxlen, wend-wstart+1)
        return maxlen
            
        
