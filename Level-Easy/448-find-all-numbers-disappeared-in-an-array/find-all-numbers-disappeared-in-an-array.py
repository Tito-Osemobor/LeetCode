from collections import Counter

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        counter1 = Counter(nums)
        counter2 = Counter(list(range(1, len(nums) + 1)))

        result = list((counter2 - counter1).elements())
        return(result)