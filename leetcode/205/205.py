class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        iso_dict_t_2_s = {}
        for i in range(len(t)):
            if t[i] not in iso_dict_t_2_s:
                iso_dict_t_2_s[t[i]] = s[i]
            else:
                if  iso_dict_t_2_s[t[i]] != s[i]:
                    return False
        iso_dict_s_2_t = {}
        for i in range(len(s)):
            if s[i] not in iso_dict_s_2_t:
                iso_dict_s_2_t[s[i]] = t[i]
            else:
                if  iso_dict_s_2_t[s[i]] != t[i]:
                    return False
        return True