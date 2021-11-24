https://leetcode.com/problems/reverse-words-in-a-string/submissions/
  
  class Solution:
    def reverseWords(self, s: str) -> str:
        answer = ""
        for string in s.split(" ")[::-1]:
            if len(string) > 0:
                answer = answer + string +" "
        return answer[0:-1]
            
        
