class Node(object):
    def __init__(self, x):
        self.val = x
        self.lchild = None
        self.rchild = None
class Tree(object):
    """二叉树"""
    def __init__(self):
        self.root = None

    def add(self,item):
        node =Node(item)

        if self.root is None:
            self.root = node
            return
        queue = [self.root]

        while queue:
            cur_node =  queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
                if cur_node.rchild is None:
                    cur_node.rchild = node
                    return
                else:
                    queue.append(cur_node.rchild)


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return vmm(root)[0]


def vmm(tree):
    """
    返回值：是不是合法的二叉搜索树，最大值，最小值
    """
    if not tree:
        return True, None, None
    else:
        lv, lmx, lmi = vmm(tree.lchild)
        rv, rmx, rmi = vmm(tree.rchild)
        if not lv or not rv:
            return False, None, None
        elif lmx and lmx >= tree.val:
            return False, None, None
        elif rmi and rmi <= tree.val:
            return False, None, None
        else:
            return True, rmx or tree.val, lmi or tree.val
tree=Tree()
tree.add(2)
tree.add(1)
tree.add(3)
a=Solution()
print(a.isValidBST(tree.root))