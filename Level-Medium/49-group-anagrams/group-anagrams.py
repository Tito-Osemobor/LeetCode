class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = defaultdict(list)
        for str in strs:
            sortedS = "".join(sorted(str))
            answer[sortedS].append(str)
        return list(answer.values())