from binarytree import Node


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.d = 0
        self.Balanced = True

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return Node(key)

        if key < root.value:
            root.left = self._insert(root.left, key)
        elif key > root.value:
            root.right = self._insert(root.right, key)

        return root

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.value == key:
            return root

        if key > root.value:
            return self._search(root.right, key)
        else:
            return self._search(root.left, key)

    def depth_first_search(self, key):
        return self._depth_first_search(self.root, key)

    def _depth_first_search(self, root, key):
        if root is None or root.value == key:
            return root

        LeftSearch = self._depth_first_search(root.left, key)
        if LeftSearch is not None:
            return LeftSearch
        else:
            return self._depth_first_search(root.right, key)

    def findDepth(self):
        return self._findDepth(self.root)

    def _findDepth(self, root):
        if root is None:
            return 0

        return 1 + max(self._findDepth(root.left), self._findDepth(root.right))

    def diameter(self):
        return self._diameter(self.root)

    def _diameter(self, root):
        if root is None:
            return 0

        left = self._findDepth(root.left)
        right = self._findDepth(root.right)

        self.d = max(self.d, left + right)

        return self.d

    def isBalanced(self):
        return self._isBalanced(self.root)

    def _isBalanced(self, root):
        if root is None:
            return

        LeftHeight = self._findDepth(root.left)
        RightHeight = self._findDepth(root.right)

        ## It should be already balanced and the current node should also be balanced
        self.Balanced = self.Balanced and (abs(LeftHeight - RightHeight) <= 1)

        return self.Balanced


# Example Usage:
bst = BinarySearchTree()
# keys = [10, 5, 15, 3, 7, 12, 18]
keys = [10, 5, 15, 12, 18]

for key in keys:
    bst.insert(key)

# Getting binary tree
print("Binary tree :", bst.root)
print("Balanced: ", bst.isBalanced())

# print(f"Diameter -> {bst.diameter()}")

# search_key = 7
# result = bst.depth_first_search(search_key)

# if result:
#     print(f"Key {search_key} found in the BST.")
# else:
#     print(f"Key {search_key} not found in the BST.")


# search_key = 14
# result = bst.depth_first_search(search_key)

# if result:
#     print(f"Key {search_key} found using DFS in the BST.")
# else:
#     print(f"Key {search_key} not found using DFS in the BST.")

# print(f"Depth of the tee -> {bst.depth}")
