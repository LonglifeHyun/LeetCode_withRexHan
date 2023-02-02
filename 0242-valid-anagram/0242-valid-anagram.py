from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        s_cnter = Counter(s)
        t_cnter = Counter(t)
        
        answer = True
        for k, v in t_cnter.items():
            if k in s_cnter:
                if s_cnter[k] != v:
                    answer = False
            else:
                answer = False
                
        return answer