class Solution:
    def reverseVowels(self, s: str) -> str:
        res = list(s)
        left, right = 0, len(res) - 1
        vowels = "aeiou"
        
        while left < right:
            # Swap the characters
            if res[left].lower() in vowels and res[right].lower() in vowels:
                res[left], res[right] = res[right], res[left]
                left += 1
                right -= 1
            else:
                if res[left].lower() not in vowels:
                    left += 1
                if res[right].lower() not in vowels:
                    right -= 1
        return "".join(res)