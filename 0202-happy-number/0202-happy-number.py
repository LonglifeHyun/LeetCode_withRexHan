class Solution(object):
    def isHappy(self, n):
        tgt_num = n
        num_map = {n:0}
        
        answer = True
        
        while(tgt_num != 1):
            nxt_num = 0
            for i in str(tgt_num):
                nxt_num += int(i) ** 2
            if int(nxt_num) in num_map:    
                answer = False
                break
            else:    
                tgt_num = nxt_num
                num_map[tgt_num] = 0
        
        return answer