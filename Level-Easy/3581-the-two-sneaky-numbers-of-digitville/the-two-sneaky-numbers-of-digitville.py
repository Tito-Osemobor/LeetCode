from collections import Counter

class Solution:
    def getSneakyNumbers(self, nums: List [int]) -> List[int]:
        return [num for num, count in Counter(nums).items() if count > 1]