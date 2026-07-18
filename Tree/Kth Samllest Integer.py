# Lowest Common Ancestor in a Binary Tree

from unittest import result


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inOrderTraversal(root: TreeNode) -> list:
    if not root:
        return []
    
    left = inOrderTraversal(root.left)
    right = inOrderTraversal(root.right)

    return left + [root.val] + right


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

    # K is 6
    result = inOrderTraversal(root)
    print(f"Original Tree In-Order Traversal: {result}") # output: [1, 2, 3, 4, 5, 6, 7, 11, 12, 13]
    print(f"Kth smallest element: {result[6-1]}")  # Output: 6