class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        quotient = []
        dividend = columnNumber
        while(dividend >26):
            quotient.append((dividend-1) %26)
            dividend = (dividend-1) // 26
        quotient.append(dividend-1)
        answer = ""
        for i in range(len(quotient)-1,-1,-1):
            answer += chr(quotient[i]+65)
        return answer
        
s = Solution()
print(s.convertToTitle(52))
