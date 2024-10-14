class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        pattern_to_word = {}
        word_to_pattern = {}

        for p, w in zip(pattern, words):
            if pattern_to_word.get(p) and pattern_to_word[p] != w:
                return False
            if word_to_pattern.get(w) and word_to_pattern[w] != p:
                return False
            pattern_to_word[p] = w
            word_to_pattern[w] = p
        return True