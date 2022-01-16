# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:  # root为空时直接返回[]
            return []
        res = []  # 返回的最终结果
        cur_nodes = [root]  # 当前访问层
        next_nodes = []  # 下一层需要访问的
        res.append([i.val for i in cur_nodes])  # 先把第一层的值放入res中
        while cur_nodes or next_nodes:  # 当前结点或下一层结点不为空
            for node in cur_nodes:  # 当前结点的所有孩子都加入next_nodes
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            if next_nodes:  # 下一层结点不为空时加入res
                res.append(
                    [i.val for i in next_nodes]
                )
            cur_nodes = next_nodes  # 更新当前结点为next_nodes
            next_nodes = []  # 下一层结点置空
        return res


right_tree = TreeNode(20)
right_tree.right=TreeNode(7)
right_tree.left=TreeNode(5)

left_tree=TreeNode(9)

tree=TreeNode(3)
tree.left=left_tree
tree.right=right_tree

a=Solution()
print(a.levelOrder(tree))