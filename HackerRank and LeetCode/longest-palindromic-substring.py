#https://leetcode.com/problems/longest-palindromic-substring/submissions/
class Solution:

    def expand(self, s,l,r):
        while l>=0 and r<len(s) and s[l] == s[r] :
            l-=1
            r+=1
        return s[l+1:r]
    
    def longestPalindrome(self, s: str) -> str:
        
        if s == None or len(s)<1:
            return ""
        
        maxlen = 0
        maxstr = ""
        
        for i in range(len(s)):
            ans1 = self.expand(s,i,i)
            ans2 = self.expand(s,i,i+1)
            
            if len(ans1) > len(ans2):
                ans= ans1
                length= len(ans1)
            else:
                ans= ans2
                length= len(ans2)
            
            if length > maxlen:
                maxlen = length
                maxstr = ans
        return maxstr
            
            
        
