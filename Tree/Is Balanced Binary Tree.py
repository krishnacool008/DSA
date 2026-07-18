
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root):

    if not root:
        return [True, 0]

    # we will use left to calculaate if left is Balanced ? and depth of left
    left, left_height = isBalanced(root.left) 
    # we will use right to calculaate if right is Balanced ? and depth of right
    right, right_height = isBalanced(root.right)

    nodeBalanced = left and right and abs(left_height - right_height) <= 1
    max_depth = 1 + max(left_height, right_height)

    # We need is current node balanced and depth of current node
    # For line number 13 and 14 
    return nodeBalanced, max_depth

# Example usage
if __name__ == "__main__":

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(4)

    print(f"Tree is balanced: {isBalanced(root)[0]}")  # Output: False