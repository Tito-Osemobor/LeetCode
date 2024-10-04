class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = ''.join(c for c in s if c.isalnum()).lower()
        return cleaned_text == cleaned_text[::-1]

        