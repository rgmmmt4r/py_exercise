from re import I


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        appearance_dict = {}
        for idx in range(len(nums)):
            if nums[idx] not in appearance_dict:
                appearance_dict[nums[idx]] = idx
            else:
                if abs(idx - appearance_dict[nums[idx]] ) <= k:
                    return True
                else:
                    appearance_dict[nums[idx]] = idx
        return False