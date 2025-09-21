import heapq
import pytest


class SmallestInfiniteSet:
    """
        You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].
        Implement the SmallestInfiniteSet class:
        SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
        int popSmallest() Removes and returns the smallest integer contained in the infinite set.
        void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.

        Example 1:
        Input
        ["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
        [[], [2], [], [], [], [1], [], [], []]
        Output
        [null, null, 1, 2, 3, null, 1, 4, 5]
        Explanation
        SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
        smallestInfiniteSet.addBack(2);    // 2 is already in the set, so no change is made.
        smallestInfiniteSet.popSmallest(); // return 1, since 1 is the smallest number, and remove it from the set.
        smallestInfiniteSet.popSmallest(); // return 2, and remove it from the set.
        smallestInfiniteSet.popSmallest(); // return 3, and remove it from the set.
        smallestInfiniteSet.addBack(1);    // 1 is added back to the set.
        smallestInfiniteSet.popSmallest(); // return 1, since 1 was added back to the set and
                                           // is the smallest number, and remove it from the set.
        smallestInfiniteSet.popSmallest(); // return 4, and remove it from the set.
        smallestInfiniteSet.popSmallest(); // return 5, and remove it from the set.
        Constraints:
        1 <= num <= 1000
        At most 1000 calls will be made in total to popSmallest and addBack.
        """

    def __init__(self):
        self.current = 1
        self.added_back = []
        self.added_back_set = set()

    def popSmallest(self) -> int:
        if self.added_back:  # take from heap if available
            smallest = heapq.heappop(self.added_back)
            self.added_back_set.remove(smallest)
            return smallest
        else:
            self.current += 1
            return self.current - 1

    def addBack(self, num: int) -> None:
        if num < self.current and num not in self.added_back_set:
            heapq.heappush(self.added_back, num)
            self.added_back_set.add(num)


@pytest.mark.parametrize("ops, args, expected", [
    (
        ["SmallestInfiniteSet", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest",
         "popSmallest"],
        [[], [], [], [1], [], [], []],
        [None, 1, 2, None, 1, 3, 4]
    ),
    (
        ["SmallestInfiniteSet", "popSmallest", "addBack", "addBack", "popSmallest"],
        [[], [], [2], [1], []],
        [None, 1, None, None, 1]
    ),
])


def test_smallest_infinite_set(ops, args, expected):
    obj = None
    results = []
    for op, arg, exp in zip(ops, args, expected):
        if op == "SmallestInfiniteSet":
            obj = SmallestInfiniteSet()
            results.append(None)
        elif op == "popSmallest":
            results.append(obj.popSmallest())
        elif op == "addBack":
            obj.addBack(arg[0])
            results.append(None)
    assert results == expected
