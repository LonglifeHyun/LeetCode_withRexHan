class Solution(object):
    def balancedStringSplit(self, s):
        cnt = 0
        stk = 0
        for c in s:
            if c == 'R':
                stk += 1
            if c == 'L':
                stk -= 1
            if stk == 0:
                cnt += 1
        return cnt
        