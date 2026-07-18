
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Build tree from list
def buildTree(values):
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

def treeToList(root):
    if not root:
        return []
    result, queue = [], [root]
    while queue:
        node = queue.pop(0)
        result.append(node.val if node else None)
        if node:
            queue.append(node.left)
            queue.append(node.right)
    while result and result[-1] is None:
        result.pop()
    return result

def invertBinaryTree(root):

    if not root:
        return
    
    invertBinaryTree(root.left)
    invertBinaryTree(root.right)

    root.left, root.right = root.right, root.left

    return root



# Example usage
root = buildTree([1,2,3,4,5,6,7])
invertBinaryTree(root)
print(treeToList(root))  # Output: [1, 3, 2, 7, 6, 5, 4]