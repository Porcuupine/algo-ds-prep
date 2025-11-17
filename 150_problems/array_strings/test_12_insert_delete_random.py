import random
import pytest


class TestRandomizedSet:
    def __init__(self):
        self.arr = []
        self.pos = {}

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        self.pos[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False

        idx = self.pos[val]
        last = self.arr[-1]

        # Move last element into the spot of the removed element
        self.arr[idx] = last
        self.pos[last] = idx

        # Remove the last element
        self.arr.pop()
        del self.pos[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)


@pytest.mark.parametrize("ops, args, expected", [
    (
        [
            "RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"
        ],
        [
            [], [1], [2], [2], [], [1], [2], []
        ],
        [
            None, True, False, True, "ANY", True, False, "ANY"
        ]
    ),
])
def test_randomized_set(ops, args, expected):
    obj = None
    random.seed(0)

    for op, arg, exp in zip(ops, args, expected):
        if op == "RandomizedSet":
            obj = TestRandomizedSet()
            continue

        if op == "insert":
            assert obj.insert(arg[0]) == exp

        elif op == "remove":
            assert obj.remove(arg[0]) == exp

        elif op == "getRandom":
            result = obj.getRandom()
            assert result in obj.arr  # cannot check exact number because it's random
