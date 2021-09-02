class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorder_traversal(root):
    """
    Algorithm Inorder(tree)
       1. Traverse the left subtree, i.e., call Inorder(left-subtree)
       2. Visit the root.
       3. Traverse the right subtree, i.e., call Inorder(right-subtree)

    example:
        1
       / \
      2   3
     / \ / \ 
    4  5 6  7
    inorder: 4 2 5 1 6 3 7
    """
    if root is None:
        return []

    left_output = []
    right_output = []

    if root.left is not None:
        left_output = inorder_traversal(root.left)

    if root.right is not None:
        right_output = inorder_traversal(root.right)

    return left_output + [root.val] + right_output


def preorder_traversal(root):
    """
    Algorithm Preorder(tree)
       1. Visit the root.
       2. Traverse the left subtree, i.e., call Preorder(left-subtree)
       3. Traverse the right subtree, i.e., call Preorder(right-subtree)

    example:
        1
       / \
      2   3
     / \ / \ 
    4  5 6  7
    preorder: 1 2 4 5 3 6 7
    """
    if root is None:
        return []

    left_output = []
    right_output = []

    if root.left is not None:
        left_output = preorder_traversal(root.left)

    if root.right is not None:
        right_output = preorder_traversal(root.right)

    return [root.val] + left_output + right_output


def postorder_traversal(root):
    """
    Algorithm Postorder(tree)
       1. Traverse the left subtree, i.e., call Postorder(left-subtree)
       2. Traverse the right subtree, i.e., call Postorder(right-subtree)
       3. Visit the root.
    
    example:
        1
       / \
      2   3
     / \ / \ 
    4  5 6  7
    postorder: 4 5 2 6 7 3 1
    """
    if root is None:
        return []

    left_output = []
    right_output = []

    if root.left is not None:
        left_output = preorder_traversal(root.left)

    if root.right is not None:
        right_output = preorder_traversal(root.right)

    return left_output + right_output + [root.val]


def breadth_first_traversal(root):
    """
    example:
        1
       / \
      2   3
     / \ / \ 
    4  5 6  7
    levelorder or bft: 1 2 3 4 5 6 7
    """

    if root is None:
        return []

    records = []
    queue = [root]

    while len(queue) > 0:
        node = queue.pop(0)
        records.append(node.val)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)

    return records


def depth_first_traversal(root):
    if root is None:
        return []

    # left_output


if __name__ == "__main__":
    root = Node(3)
    root.left = Node(2)
    root.right = Node(1)

    print(inorder_traversal(root))

    root = Node(3)
    root.right = Node(4)
    print(inorder_traversal(root))

    root = Node(3)
    root.left = Node(2)
    root.left.left = Node(1)
    root.left.right = Node(5)
    print(inorder_traversal(root))
