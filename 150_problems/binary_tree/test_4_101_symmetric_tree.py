from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values: list[int] | None) -> TreeNode:
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


def tree_list_to_list(root: TreeNode | None) -> list[int] | None:
    if not root:
        return []

    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            result.append(node.left)
            result.append(node.right)
        else:
            result.append(None)

    while result and result[-1] is None:
        result.pop()

    return result
