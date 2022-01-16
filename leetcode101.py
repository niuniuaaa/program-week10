class BTree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data


def isSymmetric(root):
    """
    :type root: TreeNode
    :rtype: bool
    """

    def f(p, q):
        if p == None:
            return q is None
        if q == None:
            return p == None
        if p.val == q.val:
            return f(p.left, q.right) and f(p.right, q.left)
        if p.val != q.val:
            return False

    if root is None:
        return True
    return f(root.left, root.right)


right_tree = BTree(2)
right_tree.right = BTree(3)

left_tree = BTree(2)
left_tree.right = BTree(3)

tree = BTree(1)
tree.left = left_tree
tree.right = right_tree

right_tree1 = BTree(2)
right_tree1.right = BTree(3)
right_tree1.left=BTree(4)

left_tree1 = BTree(2)
left_tree1.right = BTree(4)
left_tree1.left=BTree(3)

tree1 = BTree(1)
tree1.left = left_tree1
tree1.right = right_tree1
print(isSymmetric(tree))
print(isSymmetric(tree1))