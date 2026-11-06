class Solution:
    def romanToInt(self, s: str) -> int:
        hashset = {'I':1, 'V':5, 'X': 10, 'L':50, 'C': 100, 'D': 500, 'M': 1000}
        ans = 0
        n = len(s)
        flag = -1

        for i in range(n):
            if flag > 0:
                flag *= (-1)
                continue
            
            if s[i] == 'I' and i <= n-2 and s[i+1] in ['V','X']:
                if s[i+1] == 'V':
                    ans += 4
                    flag *= (-1)
                elif s[i+1] == 'X':
                    ans += 9
                    flag *= (-1)
            elif s[i] == 'X' and i <= n-2 and s[i+1] in ['L','C']:
                if s[i+1] == 'L':
                    ans += 40
                    flag *= (-1)
                elif s[i+1] == 'C':
                    ans += 90
                    flag *= (-1)

            elif s[i] == 'C' and i <= n-2 and s[i+1] in ['D','M']: 
                if s[i+1] == 'D':
                    ans += 400
                    flag *= (-1)
                elif s[i+1] == 'M':
                    ans += 900
                    flag *= (-1)

            else:
                ans += hashset[s[i]]
        return ans




