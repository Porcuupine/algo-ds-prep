import pytest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values: list[int, None]) -> TreeNode | None:
    nodes = [TreeNode(v) if v is not None else None for v in values]
    kids = nodes[::-1]

    root = kids.pop()
    for node in nodes:
        if node:
            if kids: root.left = kids.pop()
            if kids: root.right = kids.pop()
    return root


def tree_to_list(root: TreeNode | None) -> list[int | None]:
    if not root:
        return []
    out, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node:
            out.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            out.append(None)
    while out and out[-1] is None:
        out.pop()
    return out


class TestDeleteNode:
    """
    Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.
    Basically, the deletion can be divided into two stages:
    Search for a node to remove.
    If the node is found, delete the node.
    Example 1:
    Input: root = [5,3,6,2,4,null,7], key = 3
    Output: [5,4,6,2,null,null,7]
    Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
    One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
    Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.
    Example 2:
    Input: root = [5,3,6,2,4,null,7], key = 0
    Output: [5,3,6,2,4,null,7]
    Explanation: The tree does not contain a node with value = 0.
    Example 3:
    Input: root = [], key = 0
    Output: []
    """

    def delete_node(self, root: TreeNode | None, key: int) -> TreeNode | None:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node found
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            # Node has 2 children: find inorder successor (min of right subtree)
            min_node = root.right
            while min_node.left:
                min_node = min_node.left

            root.val = min_node.val
            root.right = self.deleteNode(root.right, min_node.val)

        return root

    @pytest.mark.parametrize(
        "tree_list,key,expected",
        [
            ([5, 3, 6, 2, 4, None, 7], 3, [5, 4, 6, 2, None, None, 7]),
            ([5, 3, 6, 2, 4, None, 7], 0, [5, 3, 6, 2, 4, None, 7]),
        ],
    )
    def test_delete_node(self, tree_list, key, expected):

        root = build_tree(tree_list)
        new_root = self.delete_node(root, key)
        assert self.delete_node(new_root, key) == expected
