class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res= 0
        def dfs (cur) :
            if not cur :
                return 0
            left = dfs(cur.left)
            right = dfs(cur.right)
            nonlocal res
            res = max(res,left+right)
            return 1+max(right,left)
        dfs(root)
        return res