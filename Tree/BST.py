# from binarytree import Node
from collections import deque


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return Node(key)

        if key < root.val:
            root.left = self._insert(root.left, key)
        elif key > root.val:
            root.right = self._insert(root.right, key)

        return root

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.val == key:
            return root

        if key < root.val:
            return self._search(root.left, key)
        else:
            return self._search(root.right, key)

    def depth_first_search(self, key):
        return self._depth_first_search(self.root, key)

    def _depth_first_search(self, root, key):
        if root is None or root.val == key:
            return root

        left_result = self._depth_first_search(root.left, key)
        if left_result is not None:
            return left_result

        return self._depth_first_search(root.right, key)

    def store_inorder(self, root, nodes):
        """Helper function to perform in-order traversal and store nodes."""
        if not root:
            return
        self.store_inorder(root.left, nodes)
        nodes.append(root)
        self.store_inorder(root.right, nodes)

    def build_balanced_tree(self, nodes, start, end):
        """Helper function to build a balanced tree from sorted nodes."""
        if start > end:
            return None
        mid = (start + end) // 2
        root = nodes[mid]
        root.left = self.build_balanced_tree(nodes, start, mid - 1)
        root.right = self.build_balanced_tree(nodes, mid + 1, end)
        return root

    def balance_binary_tree(self, root):
        """Main function to balance the binary tree."""
        nodes = []
        self.store_inorder(root, nodes)
        return self.build_balanced_tree(nodes, 0, len(nodes) - 1)
    
    def print_binary_tree(self, root):
        if not root:
            print("Empty Tree")
            return

        # Use BFS to get levels
        queue = deque([(root, 0)])
        levels = {}

        while queue:
            node, level = queue.popleft()
            if level not in levels:
                levels[level] = []
            levels[level].append(str(node.val) if node else " ")

            if node:
                queue.append((node.left, level + 1))
                queue.append((node.right, level + 1))
            else:
                # Add null children to preserve spacing
                queue.append((None, level + 1))
                queue.append((None, level + 1))

            # Stop if the current level is all None
            if all(n is None for n, _ in queue):
                break

        # Print the tree
        max_level = max(levels.keys())
        max_width = 2 ** (max_level + 1)
        for level in range(max_level + 1):
            space = " " * (max_width // (2 ** (level + 1)))
            line = space.join(levels[level])
            print(" " * (max_width // (2 ** level)) + line)

    def binary_tree_to_array(self, root):
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)

        # Optional: Trim trailing None values for a cleaner array
        while result and result[-1] is None:
            result.pop()

        return result

    

# Example Usage:
bst = BinarySearchTree()
keys = [1,2,3,4]

for key in keys:
    bst.insert(key)

print(bst.binary_tree_to_array(bst.root))  
root = bst.balance_binary_tree(bst.root)
print("-------------------------------------------------------------------------------")
print(bst.binary_tree_to_array(root))   