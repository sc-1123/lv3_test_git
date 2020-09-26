from queue import Queue
import sys

class BinaryTreeNode:
    def __init__(self, data, l=None, r=None):
        self.data = data
        self.left = l
        self.right = r
    def clone(self):
        new_node = BinaryTreeNode(self.data)
        if self.left:
            new_node.left=self.left.clone()
        if self.right:
            new_node.right=self.right.clone()
        return new_node

class BinaryTree:
    root:BinaryTreeNode
    def __init__(self, node):
        self.root = node
    def insert_left(self, value):
        node = BinaryTreeNode(value)
        if self.root is None:
            self.root = node
        else:
            if not self.root.left:
                self.root.left = node
            else:
                node.left = self.root.left
                self.root.left = node

    def insert_right(self, value):
        node = BinaryTreeNode(value)
        if self.root is None:
            self.root = node
        else:
            if not self.root.right:
                self.root.right = node
            else:
                node.right = self.root.right
                self.root.right = node

    def pre_order(self):
        def pre_order_helper(node):
            if node:
                print(node.data)
                pre_order_helper(node.left)
                pre_order_helper(node.right)

        cur = self.root
        pre_order_helper(cur)

    def get_height(self):
        def get_height_helper(node):
            if node is None:
                return 0

            left_height = get_height_helper(node.left)
            right_height = get_height_helper(node.right)

            return max(left_height, right_height) + 1

        return get_height_helper(self.root)

    # balanced tree: For every node, the height of the left subtree and
    # that of the right sub tree differ at most 1

    def is_balanced(self):
        def is_balanced_helper(node):
            if node is None:
                return True
            left_height = BinaryTree(node.left).get_height()
            right_height = BinaryTree(node.right).get_height()

            if abs(left_height - right_height) > 1:
                return False

            return is_balanced_helper(node.left) and is_balanced_helper(node.right)

        return is_balanced_helper(self.root)

    def is_symmetric(self):
        def is_symmetric_helper(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            if left.data != right.data:
                return False

            return is_symmetric_helper(left.left, right.right) and is_symmetric_helper(left.right, right.left)

        if self.root is None:
            return True
        return is_symmetric_helper(self.root.left, self.root.right)

    def display(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        def display_helper(node):
            if node.right is None and node.left is None:
                line = '%s' % node.data
                width = len(line)
                height = 1
                middle = width // 2
                return [line], width, height, middle

            # Only left child.
            if node.right is None:
                lines, n, p, x = node.left.display()
                s = '%s' % node.data
                u = len(s)
                first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
                second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
                shifted_lines = [line + u * ' ' for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

            # Only right child.
            if node.left is None:
                lines, n, p, x = display_helper(node.right)
                s = '%s' % node.data
                u = len(s)
                first_line = s + x * '_' + (n - x) * ' '
                second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
                shifted_lines = [u * ' ' + line for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

            # Two children.
            left, n, p, x = display_helper(node.left)
            right, m, q, y = display_helper(node.right)
            s = '%s' % node.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
            second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
            if p < q:
                left += [n * ' '] * (q - p)
            elif q < p:
                right += [m * ' '] * (p - q)
            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
            return lines, n + m + u, max(p, q) + 2, n + u // 2

        if self.root:
            lines, _, _, _ = display_helper(self.root)
            for line in lines:
                print(line)
    def clone(self):
        if self.root:
            return BinaryTree(self.root.clone())
        else:
            return BinaryTree(None)





tree = BinaryTree(BinaryTreeNode(1))
tree.root.left = BinaryTreeNode(2)
tree.root.right = BinaryTreeNode(5)
tree.root.left.left = BinaryTreeNode(3)
tree.root.left.right = BinaryTreeNode(4)
tree.root.right.left = BinaryTreeNode(6)
tree.root.right.right = BinaryTreeNode(7)

tree.pre_order()
print(tree.get_height())

print(tree.is_balanced())
print(tree.display())
tree.clone().display()