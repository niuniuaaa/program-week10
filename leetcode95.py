# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def PrintTree(self):
        print(self.val),
        if self.left:
            self.left.PrintTree()
        if self.right:
            self.right.PrintTree()


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if not n: return []
        nodes = list(range(1, n + 1))
        return gt(nodes)


def gt(nodes):
    if not nodes:
        return [None]
    trees = []
    for idx, item in enumerate(nodes):
        for left in gt(nodes[:idx]):
            for right in gt(nodes[idx + 1:]):
                trees.append(TreeNode(item, left, right))
    return trees


a = Solution()
for i in range(len(a.generateTrees(3))):
    root = a.generateTrees(3)[i]
    print(root.val)
    root.PrintTree()
    print("\n")
