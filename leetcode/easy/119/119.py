class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        totaList = [[1],[1,1]]
        for row in range(2,rowIndex+1):
            temp_row = [1]
            for i in range(row-1):
                temp_num = totaList[row-1][i] + totaList[row-1][i+1]
                temp_row.append(temp_num)
            temp_row.append(1)
            totaList.append(temp_row)
        return totaList[rowIndex]

s = Solution()

print(s.getRow(11))
        