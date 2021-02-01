#https://leetcode.com/problems/minimum-window-substring/submissions/
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        length = len(s)
        wstart=0
        tdict = {}
        valid = False
        
        for c in t:
            if c in tdict.keys():
                tdict[c] +=1
            else:
                tdict[c] = 1
        
        firstrundone = False
        for wend in range(length):
            
            if s[wend] in tdict.keys():
                tdict[s[wend]] -= 1
                valid = True
                # print(tdict,wstart,wend)
                #checking validity
                for keys,values in tdict.items():
                    if values > 0:
                        valid=False
                        break   
                if valid == True:
                    while s[wstart] not in tdict.keys() or (s[wstart] in tdict.keys() and tdict[s[wstart]]) <0:
                        if s[wstart] in tdict.keys() and tdict[s[wstart]] <0:
                            tdict[s[wstart]] += 1
                        wstart +=1
                    print(tdict,wstart,wend)
                    if firstrundone is False:
                        minlen = wend - wstart + 1
                        left = wstart
                        right = wend
                        firstrundone = True
                        print(s[left:right+1])
                    else:
                        currentlen = wend - wstart + 1
                        print(currentlen)
                        if currentlen < minlen:
                            left = wstart
                            right = wend
                            minlen = currentlen

                    while s[wstart] not in tdict.keys() or (s[wstart] in tdict.keys() and tdict[s[wstart]]) <=0:
                        if s[wstart] in tdict.keys() and tdict[s[wstart]] <=0:
                            tdict[s[wstart]] += 1
                            if tdict[s[wstart]] >0:
                                wstart +=1
                                break
                        wstart +=1

        if firstrundone==True:
            return s[left:right+1]
        else:
            return ""
