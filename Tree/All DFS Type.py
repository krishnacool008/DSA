# Lowest Common Ancestor in a Binary Tree

from unittest import result


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# In-Order Traversal - Version 1 (returns a new list)
def inOrderTraversalv1(root: TreeNode) -> list:
    if not root:
        return []

    left = inOrderTraversalv1(root.left)
    right = inOrderTraversalv1(root.right)

    return left + [root.val] + right
# In-Order Traversal - Version 2 (modifies an existing list)
def inOrderTraversalv2(root: TreeNode, result: list) -> list:
    if not root:
        return

    inOrderTraversalv2(root.left, result)
    result.append(root.val)
    inOrderTraversalv2(root.right, result)



# Pre-Order Traversal - Version 1 (returns a new list)
def preOrderTraversalv1(root: TreeNode) -> list:
    if not root:
        return []

    left = preOrderTraversalv1(root.left)
    right = preOrderTraversalv1(root.right)

    return [root.val] + left + right
# Pre-Order Traversal - Version 2 (modifies an existing list)
def preOrderTraversalv2(root: TreeNode, result: list) -> list:
    if not root:
        return

    result.append(root.val)
    preOrderTraversalv2(root.left, result)
    preOrderTraversalv2(root.right, result)


# Post-Order Traversal - Version 1 (returns a new list)
def postOrderTraversalv1(root: TreeNode) -> list:
    if not root:
        return []

    left = postOrderTraversalv1(root.left)
    right = postOrderTraversalv1(root.right)

    return left + right + [root.val]
# Post-Order Traversal - Version 2 (modifies an existing list)
def postOrderTraversalv2(root: TreeNode, result: list) -> list:
    if not root:
        return

    postOrderTraversalv2(root.left, result)
    postOrderTraversalv2(root.right, result)
    result.append(root.val)

# Example usage
if __name__ == "__main__":
    # Create first tree
    root = TreeNode(7)
    root.left = TreeNode(4)
    root.right = TreeNode(12)

    root.right.left = TreeNode(11)
    root.right.right = TreeNode(13)

    root.left.left = TreeNode(2)
    root.left.right = TreeNode(6)

    root.left.right.left = TreeNode(5)

    root.left.left.left = TreeNode(1)
    root.left.left.right = TreeNode(3)

    # result = []
    # inOrderTraversal(root, result)
    print(f"Original Tree Pre-Order Traversal: {preOrderTraversalv1(root)}") # output: [7, 4, 2, 1, 3, 6, 5, 12, 11, 13]
    print(f"Original Tree In-Order Traversal: {inOrderTraversalv1(root)}") # output: [1, 2, 3, 4, 5, 6, 7, 11, 12, 13]
    print(f"Original Tree Post-Order Traversal: {postOrderTraversalv1(root)}") # output: [1, 3, 2, 5, 6, 4, 11, 13, 12, 7]

    # print(f"Kth smallest element: {result[2]}")  # Output: 5