class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        majority_count = len(nums) // 2
        answer = 0
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
            if dict[num] > majority_count:
                answer = num
        return answer
        