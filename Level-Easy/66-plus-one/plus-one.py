class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans=0
        for i in range(0, len(digits)):
            ans=ans*10+digits[i]
        ans+=1
        return [int(digit) for digit in str(ans)]
        