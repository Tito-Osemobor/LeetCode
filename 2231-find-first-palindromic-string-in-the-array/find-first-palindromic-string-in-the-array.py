class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i, word in enumerate(words):
            if word == word[::-1]:
                return word
        return ""