class Solution:
    def bfs(self,nums,i,j):
        if i> j:
            return None
        mid = (i+j)//2
        root = nums[mid]
        root.left = self.bfs(self,nums,i,mid)
        root.right = self.bfs(self,nums,mid+1,j)
        return root

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return bfs(self,nums,0,len(nums)-1)
