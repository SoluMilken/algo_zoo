import sys

MAX_INT = sys.maxsize


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def validate_bst(root):
    # tree: no cycle
    # unique
    # left subtree < root.val < right subtree

    return dfs(root, -MAX_INT, MAX_INT)


def dfs(root, lbound, ubound):
    if root is None:
        return True

    left_output = True
    right_output = True

    if root.left is not None:
        if (root.left.val >= root.val) or (root.left.val <= lbound):
            return False
        left_output = dfs(root.left, lbound, root.val)

    if root.right is not None:
        if (root.right.val <= root.val) or (root.right.val >= ubound):
            return False
        right_output = dfs(root.right, root.val, ubound)

    return left_output and right_output


def delete_node(root, target):
    # search
    # case1 (leaf): remove it
    # case2 (has only one child): target node -> its child
    # case3 (has two childern):
    # find the (inorder successor of the right child *)
    # copy the value of * (succ_value) and remove *
    # target.node.val = succ_value
    parent_node, category = search(root, target)
    if category == "this":  # target node is root
        if (root.left is None) and (root.right is None):
            return
        if (root.left is not None) and (root.right is not None):
            # case 3
            pass
        if root.left is None:  # case 2
            return root.right
        return root.left

        if category == "left":
            target_node = parent_node.left
        else:
            target_node = parent_node.right

        # case 1 leaf
    if (target_node.left is None) and (target_node.right is None):
        if category == "left":
            parent_node.left = None
        else:
            parent_node.right = None
        return root

    # case 3
    if (target_node.left is not None) and (target_node.right is not None):
        pass
        # return

    if target_node.left is None:
        if category == "left":
            parent_node.left = target_node.right
        else:
            parent_node.right = target_node.right
    else:
        if category == "left":
            parent_node.left = target_node.left
        else:
            parent_node.right = target_node.left


def search(root, target):
    # assume that root is not None
    # return parent node and 'left' or 'right' or 'this'
    if root.val == target:
        return root, "this"
    elif target < root.val:
        if root.left is not None:
            if root.left.val == target:
                return root, "left"
            return search(root.left, target)
    else:
        if root.right is not None:
            if root.right.val == target:
                return root, "right"
            return search(root.right, target)

    # if root.right

    # if target == root.val:
    #     return root
    # elif target > root.val:
    #     return search(root.right, target)
    # return search(root.left, target)


def inorder_traversal(parent, node, category: Union["left", "right"]):
    if (node.left is None) and (node.right is None):  # leaf
        output_value = node.val
        if category == "left":
            parent.left = None
        else:
            parent.right = None
        return output_value

    if node.left is not None:
        return inorder_traversal(node, node.left, "left")

    if node.right is not None:
        return inorder_traversal(node, node.right, "right")


if __name__ == "__main__":

    #     5
    #    / \
    #   3   8
    #  / \
    # 1   4

    root = Node(5)
    root.left = Node(3)
    root.right = Node(8)

    print(validate_bst(root))

    # root.left.right = Node(8)
    root.right.left = Node(2)
    print(validate_bst(root))
