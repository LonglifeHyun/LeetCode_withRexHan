class Solution(object):
    def romanToInt(self, s):
        my_map = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000 }
        rslt_sum = 0
        i = 0
        while(i < len(s)-1):
            if int(my_map[s[i+1]]) > int(my_map[s[i]]):
                rslt_sum += (my_map[s[i+1]] - my_map[s[i]])
                i += 2
            else :
                rslt_sum += int(my_map[s[i]])
                i += 1
        if (i != len(s)):
            rslt_sum += int(my_map[s[i]])
        return rslt_sum
            
        