class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        # 将新值与父节点进行比较
        if self.data:  # 非空
            if data < self.data:  # 新值较小，放左边
                if self.left is None:  # 若空，则新建插入节点
                    self.left = Node(data)
                else:  # 否则，递归往下查找
                    self.left.insert(data)
            elif data > self.data:  # 新值较大，放右边
                if self.right is None:  # 若空，则新建插入节点
                    self.right = Node(data)
                else:  # 否则，递归往下查找
                    self.right.insert(data)
        else:
            self.data = data

    # 打印这棵树，中序遍历
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        array = []
        h(root, array)
        return array


def h(root, array):
    if root:
        h(root.left, array)
        array.append(root.data)
        h(root.right, array)


# 使用insert方法添加节点
root = Node(1)
#root.insert(None)/
root.insert(3)
root.insert(2)
print(root.inorderTraversal(root))
#root.PrintTree()