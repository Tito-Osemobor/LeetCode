class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1
            if digits[i] == 10:
                digits[i] = 0
            else:
                return digits
        return [1] + digits
        