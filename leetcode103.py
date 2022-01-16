# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []

        ans = [[]]
        queue = [(root, 0)]
        level = 0
        left2right = True
        while queue:
            node, lv = queue.pop(0)
            if lv == level:
                if left2right:
                    ans[-1].append(node.val)
                else:
                    ans[-1].insert(0, node.val)
            else:
                level = lv
                left2right = not left2right
                ans.append([node.val])
            if node.left: queue.append((node.left, lv + 1))
            if node.right: queue.append((node.right, lv + 1))
        return ans


right_tree = TreeNode(20)
right_tree.right = TreeNode(7)
right_tree.left = TreeNode(15)

left_tree = TreeNode(9)

tree = TreeNode(3)
tree.left = left_tree
tree.right = right_tree

a = Solution()
print(a.zigzagLevelOrder(tree))
