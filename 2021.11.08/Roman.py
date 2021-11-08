#https://leetcode.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        value = 0
        l = len(s)
        #先不管像是「IＸ」的減項，先算s中的所有字母的總和，等加完之後再處理減項
        for i in range(l):
            value = value + d[s[i]]
        #列出所有減項，再分別減去減項，由於在上個步驟中，已經把像是「IＸ」中的I當作是加項了，所以要減兩倍才會是正解
        for j in range(1,l):
            if s[j] == "V" or s[j] ==  "X":
                if s[j-1] == "I":
                    value = value - 2
            elif s[j] == "L" or  s[j] == "C":
                if s[j-1] == "X":
                    value = value - 20
            elif s[j] == "D" or s[j] == "M":
                if s[j-1] == "C":
                    value = value - 200
        return value
s = Solution()
a = s.romanToInt("LVIII")
print(a)
