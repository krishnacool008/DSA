class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root):

    # Return inf and -inf for min and max for null nodes
    # So that parent node is always balanced with null nodes
    if not root:
        return True, float('inf'), float('-inf')

    # We need max of left and min of left and if left is valid BST
    left_is_bst, left_min_val, left_max_val = isValidBST(root.left)
    # We need max of right and min of right and if right is valid BST
    right_is_bst, right_min_val, right_max_val = isValidBST(root.right)

    # Check if current node is BST
    current_is_bst = (
        left_is_bst and
        right_is_bst and
        left_max_val < root.val < right_min_val
    )

    # Check if min of left subtree, right subtree, and root needed on line 11 and 12
    current_min = min(left_min_val, right_min_val, root.val)
    # Check if max of left subtree, right subtree, and root needed on line 11 and 12
    current_max = max(left_max_val, right_max_val, root.val)

    # Returning value for line number 11 and 12
    return current_is_bst, current_min, current_max

# Example usage
if __name__ == "__main__":

    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)

    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)

    print(f"Tree is valid BST: {isValidBST(root)[0]}")  # Output: False