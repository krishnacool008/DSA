
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSame(root1, root2):

    if not root1 and not root2: # both are None
        return True
    elif not root1 or not root2: # one is None, other is not
            return False

    # As we have seen we call recursion first then main logic
    left = isSame(root1.left, root2.left)
    right = isSame(root1.right, root2.right)

    # left subtree should be same, right subtree should be same 
    # and current node value should be same
    if left and right and root1.val == root2.val:
        return True
    return False

# Example usage
if __name__ == "__main__":
    # Create first tree
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    
    # Create identical second tree
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    
    print(f"Trees are identical: {isSame(root1, root2)}")  # Output: True