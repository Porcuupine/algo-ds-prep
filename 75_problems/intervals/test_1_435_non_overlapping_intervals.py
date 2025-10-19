import pytest


class TestNonOverlappingIntervals:
    """
    Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
    Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.
    Example 1:
    Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
    Output: 1
    Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
    Example 2:
    Input: intervals = [[1,2],[1,2],[1,2]]
    Output: 2
    Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
    Example 3:
    Input: intervals = [[1,2],[2,3]]
    Output: 0
    Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
    Constraints:
    1 <= intervals.length <= 105
    intervals[i].length == 2
    -5 * 104 <= starti < endi <= 5 * 104
    """

    def non_overlapping_intervals(self, intervals: list[list[int]]) -> int:

        # bruteforce solution. Time: O(n²) — because of repeated popping and pair comparisons.
        # Space: O(1) (in-place).
        if not intervals:
            return 0

            # Sort by start time first
        intervals.sort(key=lambda x: x[0])
        removed = 0

        i = 0
        while i < len(intervals) - 1:
            start1, end1 = intervals[i]
            start2, end2 = intervals[i + 1]

            # If they overlap:
            if start2 < end1:
                removed += 1
                # Remove the one with the larger end
                if end1 > end2:
                    intervals.pop(i)
                else:
                    intervals.pop(i + 1)
            else:
                i += 1  # move to next pair

        return removed

    @pytest.mark.parametrize("intervals, expected", [
        ([[1, 2], [2, 3], [3, 4], [1, 3]], 1),
        ([[1, 2], [1, 2], [1, 2]], 2),
        ([[1, 2], [2, 3]], 0),
    ])
    def test_non_overlapping_intervals(self, intervals, expected):
        assert self.non_overlapping_intervals(intervals) == expected
