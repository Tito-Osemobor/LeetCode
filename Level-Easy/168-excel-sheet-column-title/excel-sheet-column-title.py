class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        output = ""
        while columnNumber > 0:
            output = chr(65 + (columnNumber - 1) % 26) + output
            columnNumber = (columnNumber - 1) // 26
        return output