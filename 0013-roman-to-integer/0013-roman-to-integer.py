class Solution(object):
    def romanToInt(self, s):
        my_map = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000 }
        rslt_sum = 0
        i = 0
        while(i < len(s)-1):
            # 들어온 문자열을 하나씩 보는데 2개를 대상으로 먼저 봄. 
            if int(my_map[s[i+1]]) > int(my_map[s[i]]):
                # 만약 2개가 역순이다? 그럼 두개를 빼기해서 더함.
                rslt_sum += (my_map[s[i+1]] - my_map[s[i]])
                i += 2 # 반복문은 2개 다음꺼부터 봐야하니까 2 증가
            else :
                # 역순이 아니었다면, 보고있는 타겟 하나만 그냥 더함.
                rslt_sum += int(my_map[s[i]])
                i += 1
        # 맨끝 2개가 역순이었던 경우엔 i == len(s)이고 계산이 종료된 상태.
        if (i != len(s)): 
            # 마지막꺼 누락되지 않게 챙겨야 함.
            rslt_sum += int(my_map[s[i]])
        return rslt_sum
            
        
