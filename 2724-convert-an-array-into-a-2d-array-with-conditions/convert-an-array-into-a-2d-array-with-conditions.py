class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        dic = {}
        ans = [[]]
        max = 0
        for num in nums:
            if num not in dic:
                dic[num] = 0
            else:
                dic[num] += 1
                if dic[num] > max:
                    ans.append([])
                    max = dic[num]
            ans[dic[num]].append(num)
        return ans
                