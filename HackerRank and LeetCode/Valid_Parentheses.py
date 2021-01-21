class Solution:
    def isValid(self, s: str) -> bool:
        originalLength = len(s)
        if originalLength %2 != 0:
            return False
        
        if originalLength == 2:
            if (s[0]=='(' and s[1]==')') or \
            (s[0]=='{' and s[1]=='}') or \
            (s[0]=='[' and s[1]==']'):
                return True
 
        i = 0
        while i < originalLength -1:
            if (s[i]=='(' and s[i+1]==')') or \
            (s[i]=='{' and s[i+1]=='}') or \
            (s[i]=='[' and s[i+1]==']'):
                s = s[0:i]+s[i+2:]
                break
            i += 1
        if len(s) == originalLength:
            return False
        
        return self.isValid(s)
        