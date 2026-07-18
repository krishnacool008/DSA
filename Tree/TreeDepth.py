
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root):
    global result
    result = 0

    if not root:
        return 0

    left_depth = diameterOfBinaryTree(root.left) # Get the depth of left subtree line 21
    right_depth = diameterOfBinaryTree(root.right) # Get the depth of left subtree line 21

    result = max(result, left_depth + right_depth) # Update the diameter if the path through the root is larger

    # Return the max depth of the tree which is needed 
    # Which is needed in line 14 and 15
    max_depth = 1 + max(left_depth, right_depth) 

    return max_depth

# Example usage
if __name__ == "__main__":
    # Create a sample tree:
    #       1
    #      / \
    #     2   3
    #    /
    #   4
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print(f"Tree depth: {diameterOfBinaryTree(root)}")  # Output: 3