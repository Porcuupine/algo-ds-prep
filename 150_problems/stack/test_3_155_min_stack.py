import pytest


class TestMinStack:
    """
    Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
    Implement the MinStack class:
    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.
    You must implement a solution with O(1) time complexity for each function.

    Example 1:
    Input
    ["MinStack","push","push","push","getMin","pop","top","getMin"]
    [[],[-2],[0],[-3],[],[],[],[]]
    Output
    [null,null,null,null,-3,null,0,-2]
    Explanation
    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin(); // return -3
    minStack.pop();
    minStack.top();    // return 0
    minStack.getMin(); // return -2
    Constraints:
    -231 <= val <= 231 - 1
    Methods pop, top and getMin operations will always be called on non-empty stacks.
    At most 3 * 104 calls will be made to push, pop, top, and getMin.
    """

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> int:
        self.stack.append(val)
        if self.min_stack:
            self.min_stack.append(min(val, self.min_stack[-1]))
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def getMin(self) -> int:
        return self.min_stack[-1]

    def top(self) -> int:
        return self.stack[-1]


@pytest.mark.parametrize(
    "operations, values, expected",
    [
        (
            ["push", "push", "push", "getMin", "pop", "top", "getMin"],
            [(-2,), (0,), (-3,), (), (), (), ()],
            [-3, 0, -2],  # expected outputs for getMin/top/getMin
        ),
        (
            ["push", "push", "getMin", "push", "getMin"],
            [(2,), (1,), (), (3,), ()],
            [1, 1],
        ),
    ],
)
def test_min_stack(operations: list[str], values: list[tuple], expected: list[int]):
    ms = TestMinStack()
    results = []
    for op, val in zip(operations, values):
        if op == "push":
            ms.push(*val)
        elif op == "pop":
            ms.pop()
        elif op == "top":
            results.append(ms.top())
        elif op == "getMin":
            results.append(ms.getMin())
    assert results == expected
