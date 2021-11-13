#https://leetcode.com/problems/longest-common-prefix/
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        '''  
        if len(strs[0]) == "":
            return ""
       
        #找出最短的strs[i]
        shortest = strs[0]
        for i in range(len(strs)):
            if len(strs[i]) < len(shortest):
                shortest = strs[i]
        '''
       
        shortest = min(strs,key = len)
              
        
        #檢查shortest是不是空的        
        l = len(shortest) 
        if l == 0:
            return ""
        #分別比較每個 strs[i][:l]和shortest，如果不一樣，shortest即變短一個字元，直到找出最短的common prefix 或是shortest變成空字串
        n = len(strs)
        for i in range(n):
            while(l>0):
                if strs[i][:l] != shortest:
                    shortest = shortest[:l-1]
                    l = len(shortest)
                else:
                     break
        return shortest
            

s = Solution()
a = s.longestCommonPrefix(["ka","b","a"])
print(a)