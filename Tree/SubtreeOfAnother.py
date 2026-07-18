
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSubtree(root, subroot):

    # An empty tree is always a subtree
    if not subroot:
        return True
    # If main tree is empty and subtree is not, return False
    if not root:
        return False

    # Calling recursion first as we have seen
    left = isSubtree(root.left, subroot) # Check if left subtree has the subtree
    right = isSubtree(root.right, subroot) # Check if right subtree has the subtree

    # Check if current node's tree is same as subroot
    if isSame(root, subroot):
        return True

    # If left or right subtree has the subtree, return True
    return left or right

def isSame(root1, root2):

    if not root1 and not root2: # both are None
        return True
    if not root1 or not root2: # one is None, other is not
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
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    
    # Create subtree
    root2 = TreeNode(2)
    root2.left = TreeNode(4)
    root2.right = TreeNode(5)

    print(f"Trees are identical: {isSubtree(root1, root2)}")  # Output: True