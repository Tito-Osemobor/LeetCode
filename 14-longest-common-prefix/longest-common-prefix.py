class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            c = strs[0][i]
            for s in strs[1:]:
                if len(s) == i or s[i] != c:
                    return strs[0][0:i] 
        return strs[0]