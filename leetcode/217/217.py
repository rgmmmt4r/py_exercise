
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        appearnaceSet = set()
        for i in nums:
            if i not in appearnaceSet:
                appearnaceSet.add(i)
            else:
                return True
        return False