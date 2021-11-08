#https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        n = len(strs)
        #先處理strs 中只有一個元素的情況
        if n == 1:
            if strs[0] == "":
                return ""
            else:
              return strs[0]
        elif n == 0:     
            return ""
        d = {}         # d 用於存每個 str[0] 中的每個 prefix，key 即是str[0]的每個prefix，value 即是該prefix出現次數
        max_value = 0  # 用於存出現最多次的 prefix，其出現的次數
        max_key = ""   # 用於存出現最多次的 prefix

        #先將str[0] 中的每個prefix 存入 d
        for j in range(1,len(strs[0])+1):
            d[strs[0][0:j]] = 1
        #在計算每個str[i]，共同出現的最長prefix
        for i in range(1,n):
            if strs[i] == "":   #如果其中有個str[i] 是 "" ，即可確認沒有common prefix
                    return ""
            for j in range(1,len(strs[i])+1):
                if strs[i][0:j] in d: #如果確認同樣prefix 出現在 str[i][0:j]，d[strs[i][0:j]] 即加一
                    d[strs[i][0:j]] =  d[strs[i][0:j]] + 1 
                    if d[strs[i][0:j]]  >=  max_value: #比較出最多次的 common prefix
                        max_key = strs[i][0:j]
                        max_value = d[strs[i][0:j]]

        if max_key != "":
            for i in range(1,n):
                if strs[i][0] != max_key[0]: #處理input 像是["aa","aa","b"] 的情況
                        return ""
        return max_key

s = Solution()
a = s.longestCommonPrefix(["aaa","aa","aaa"])
print(a)
