# https://leetcode.com/problems/find-all-anagrams-in-a-string/
class Solution:
    def isAnagram(self, a:str, b:str) -> bool:        
        if a == b:
            return True
        else: return False
        
    def findAnagrams(self, s: str, p: str) -> List[int]:
        answer = []
        plen = len(p)
        slen = len(s)
        
        if plen > slen:
            return answer
        
        pmap = [0 for _ in range(26)]
        cmap = [0 for _ in range(26)]

        for letter in p:
            pmap[ord(letter)-97] += 1
        
        
        for i in range(plen):
            cmap[ord(s[i])-97] += 1 
        
        
        if self.isAnagram(pmap,cmap):
            answer.append(0)
            
        start,end = 0 , plen-1
        
        while end < slen -1 :
            cmap[ord(s[start])-97] -=1
            start+=1
            end+=1   
            cmap[ord(s[end])-97] +=1
            if self.isAnagram(pmap,cmap):
                answer.append(start)
        return answer

        
        
        
        
