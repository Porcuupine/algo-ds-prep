class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        curr = root

        while curr:
            if curr.left:
                rightmost = curr.left
                while rightmost.right:
                    rightmost = rightmost.right

                rightmost.right = curr.right

                curr.right = curr.left
                curr.left = None
            curr = curr.right


def build_tree(values):
    if not values:
        return None
    nodes = [None if v is None else TreeNode(v) for v in values]

    for i in range(len(values)):
        if nodes[i] is None:
            continue
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(values):
            nodes[i].left = nodes[left]
        if right < len(values):
            nodes[i].right = nodes[right]

    return nodes[0]


def flatten_to_list(root):
    result = []
    while root:
        result.append()
