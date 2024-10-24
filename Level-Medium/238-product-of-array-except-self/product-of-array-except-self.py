class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        found = 0
        ans = []
        for i in nums:
            if i != 0:
                total *= i
            else:
                found += 1
        if found > 1:
            return [0]*len(nums)
        if found == 1:
            for i in nums:
                if i != 0:
                    ans.append(0)
                else:
                    ans.append(total)
            return ans
        for i in nums:
            ans.append(int(total/i))
        return ans