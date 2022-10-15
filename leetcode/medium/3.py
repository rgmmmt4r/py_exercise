class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_set = set()
        str_temp = ""
        maxlen = 0
        templen = 0
        for i in range(len(s)):
            if s[i] in str_set:
                if templen > maxlen:
                    maxlen = templen
                j = len(str_temp)
                while str_temp[j-1] != s[i]:
                    j = j -1
                str_temp = str_temp[j:] +  s[i]
                str_set = set()
                for k in range(len(str_temp)):
                    str_set.add(str_temp[k])
                templen = len(str_temp)
            else:
                str_set.add(s[i])
                str_temp += s[i]
                templen +=1
                if templen > maxlen:
                    maxlen = templen
        return maxlen


s = Solution()
print(s.lengthOfLongestSubstring("aabaab!bb"))

