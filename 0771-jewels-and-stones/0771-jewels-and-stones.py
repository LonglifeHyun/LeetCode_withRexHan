from collections import Counter

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        answer = 0
        
        stones_cnter = Counter(stones)
        
        for jewel in jewels:
            answer += stones_cnter[jewel]
            
        return answer