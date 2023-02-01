from collections import defaultdict
from collections import Counter

class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        answer = ""
        tgt_dict = defaultdict(int)

        for c in licensePlate.lower():
            if 'a' <= c and c <='z':
                tgt_dict[c] += 1
        
        min_len = 16
        for word in words:
            isComplete = True
            tmp_cnter = Counter(word)
            
            for k, v in tgt_dict.items():
                if tmp_cnter[k] < v:
                    isComplete = False
                    break
            
            if isComplete:
                if len(word) < min_len:
                    answer = word
                    min_len = len(word)
                    
        return answer