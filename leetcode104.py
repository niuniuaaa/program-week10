# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = 0
        if root == None:
            return ans
        st = []
        st.append(root)
        # temp, gp = st[0], st[0]
        gp = st[0]
        ans += 1
        while len(st) != 0:
            temp = st[0]
            if temp.left != None:
                st.append(temp.left)
            if temp.right != None:
                st.append(temp.right)

            if gp == temp:
                gp = st[len(st) - 1]
                if gp != st[0]:
                    ans += 1
            st.pop(0)
        return ans


right_tree = TreeNode(20)
right_tree.right = TreeNode(7)
right_tree.left = TreeNode(15)

left_tree = TreeNode(9)

tree = TreeNode(3)
tree.left = left_tree
tree.right = right_tree

a = Solution()
print(a.maxDepth(tree))
