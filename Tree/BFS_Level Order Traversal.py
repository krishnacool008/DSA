# Lowest Common Ancestor in a Binary Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def BFS_LevelOrderTraversal(root):

    # Import deque for efficient queue operations
    from collections import deque 
    # This is the final big array to hold all levels
    result = []

    if not root:
        return []
    
    # Initialize queue for BFS with the root node
    queue = deque([root])

    # Until we have queue
    while queue:
        # First we will check how many elements
        # Are there in queue currently
        level_size = len(queue)

        # Create an array with same size
        # Here we creating list 
        # And we will append element times the length
        current_level = []

        # Insert element in array 
        # Total elements are of length of queue
        for _ in range(level_size):
            # Pop the first element from queue
            node = queue.popleft()
            # Append it to array
            current_level.append(node.val)

            # Check if has children then add it to queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result

# Example usage
if __name__ == "__main__":
    # Create first tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    root.left.left.left = TreeNode(8)
    root.left.left.right = TreeNode(9)

    result = BFS_LevelOrderTraversal(root)
    print("Level Order Traversal:")
    for level in result:
        print(level)