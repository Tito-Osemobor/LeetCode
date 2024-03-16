class Solution:
    def romanToInt(self, s: str) -> int:
        
        ans = 0

        conversion = {
            'I':1, 
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
            }

        # IX
        for i in range(len(s)):
            if i < len(s) -  1 and conversion[s[i]] < conversion[s[i+1]]:
                ans -= conversion[s[i]]
            else:
                ans += conversion[s[i]]

        return ans