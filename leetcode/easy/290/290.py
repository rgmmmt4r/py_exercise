class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        i = 0
        str_dict = {}

        s = s.split(" ")
        if len(pattern) != len(s):
            return False
        while i < len(pattern):
            if pattern[i] not in str_dict:
                str_dict[pattern[i]] = s[i]
            else:
                if  str_dict[pattern[i]] != s[i]:
                    return False
            i +=1
        i = 0
        str_dict = {}
        while i < len(pattern):
            if s[i] not in str_dict:
                str_dict[s[i]] = pattern[i]
            else:
                if  str_dict[s[i]] != pattern[i]:
                    return False
            i +=1
        return True