# Lowest Common Ancestor in a Binary Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root, p, q):
    # Base case
    if not root:
        return None
    if root.val == p or root.val == q:
        return root

    # Search in left and right subtrees
    # If we find a value in left means we found lcs in left subtree
    # so left will be the answer and vise versa for right
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    # If both left and right are non-null, current node is LCA
    # Means left child is p or q and right child is q or p
    # for example left is p and right is q
    # Means there parent is the closest node which is LCA
    if left and right:
        return root

    # If we found left means we got the answer
    # If left is null then either right is answer or null
    # If right is answer then we will return right as answer
    # And if right is null we return null cuz both are null
    # And there is no LCA in this path
    return left if left else right

# Example usage
if __name__ == "__main__":
    # Create first tree
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(8)

    root.left.left = TreeNode(1)
    root.left.right = TreeNode(4)

    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)

    root.left.left.right = TreeNode(2)
    root.left.left.left = TreeNode(6)

    lca_node = lowestCommonAncestor(root, 3, 8)
    print(f"LCA: {lca_node.val}")  # Output: 5