from calendar import c


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        columnLenght = len(columnTitle)
        answer = 0
        for i in range(columnLenght-1,-1,-1):
            answer += (ord(columnTitle[i]) -64) * 26^(columnLenght-i-1)
        return answer