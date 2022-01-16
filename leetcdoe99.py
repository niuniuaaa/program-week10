queue=[]
class BTree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        # 将新值与父节点进行比较
        if self.data:  # 非空
            if data < self.data:  # 新值较小，放左边
                if self.left is None:  # 若空，则新建插入节点
                    self.left = BTree(data)
                else:  # 否则，递归往下查找
                    self.left.insert(data)
            elif data > self.data:  # 新值较大，放右边
                if self.right is None:  # 若空，则新建插入节点
                    self.right = BTree(data)
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


class Solution:
    def recoverTree(self, root: BTree) -> None:
        """
        Do not return anything, modify root in-place instead.
        """


        def in_order(tree):
            if not tree: return
            in_order(tree.left)
            queue.append(tree)
            in_order(tree.right)

        in_order(root)
        new_queue = sorted(queue, key=lambda n: n.data)
        for x, y in zip(queue, new_queue):
            if x != y:
                x.data, y.data = y.data, x.data
                break

#root=Node(1)
#root.insert(3)
#root.insert()
#root.insert()
#root.insert(2)
# 构造二叉树, BOTTOM-UP METHOD
right_tree = BTree(2)
#right_tree.left = BTree(2)
#right_tree.right = BTree(4)

left_tree = BTree(1)
#left_tree.left = BTree(1)
#left_tree.right = BTree(3)

tree = BTree(3)
tree.left = left_tree
tree.right = right_tree

#left_tree = BTree(7)
#left_tree.left = BTree(3)
#left_tree.right = BTree(4)

#right_tree = tree # 增加新的变量
#tree = BTree(18)
#tree.left = left_tree
#tree.right = right_tree

a=Solution()
a.recoverTree(tree)
tree.PrintTree()
print(tree.data)
print(queue[2].data)