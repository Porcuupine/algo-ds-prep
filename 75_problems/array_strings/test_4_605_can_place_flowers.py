import pytest


class TestCanPlaceFlowers:
    """605. Can Place Flowers
    You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
    Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

    Example 1:
    Input: flowerbed = [1,0,0,0,1], n = 1
    Output: true

    Example 2:
    Input: flowerbed = [1,0,0,0,1], n = 2
    Output: false

    Constraints:
    1 <= flowerbed.length <= 2 * 104
    flowerbed[i] is 0 or 1.
    There are no two adjacent flowers in flowerbed.
    0 <= n <= flowerbed.length"""

    def can_place_flowers(self, flowerbed: list[int], n: int):
        if n == 0:
            return True
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (
                i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                n -= 1
                if n == 0:
                    return True
                flowerbed[i] = 1

        return False

    @pytest.mark.parametrize(
        'flowerbed, n, expected', [
            ([1, 0, 0, 0, 1], 1, True),
            ([1, 0, 0, 0, 1], 2, False),
        ]
    )
    def test_can_place_flowers(self, flowerbed, n, expected):
        assert self.can_place_flowers(flowerbed, n) == expected
