class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dict,res = {},[]
        for i,x in enumerate(groupSizes):
            dict.setdefault(x, []).append(i)
        for key, lst in dict.items():
            groups = [lst[i:i+key] for i in range(0, len(lst), key)]
            res.extend(groups)
        return res