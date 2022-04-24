class Solution:
    def isPalindrome(self, s: str) -> bool:
        removed_str = []
        for i in range(len(s)):
            if (ord(s[i]) >=65 and ord(s[i])<= 90) or ord(s[i]) >=97 and ord(s[i])<= 122: 
                removed_str.append(s[i].lower())
            elif (ord(s[i]) >=48 and ord(s[i])<= 57):
                removed_str.append(s[i])
        print(removed_str)
        if len(removed_str) == 0:
            return True
        elif len(removed_str) % 2 == 0:
            half_idx = int((len(removed_str)/2))
            print(half_idx)
            for i in range(half_idx):
                if removed_str[i] != removed_str[len(removed_str)-1-i]:
                    return False
        else:
            half_idx = int((len(removed_str)+1)/2)
            print(half_idx)
            for i in range(half_idx):
                if removed_str[i] != removed_str[len(removed_str)-1-i]:
                    return False
        return True





s = Solution()
print(s.isPalindrome("0a0"))