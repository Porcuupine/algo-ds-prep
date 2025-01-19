import pytest


class TestFindTheHighestAltitude:
    def find_the_highest_altitude(self, gain: list[int]) -> int:
        alt = [sum(gain[:i]) for i in range(len(gain))]
        return max(alt)

    @pytest.mark.parametrize(
        'gain, expected', [
            ([-5, 1, 5, 0, -7], 1),
            ([-4,-3,-2,-1,4,3,2], 0),
        ]
    )
    def test_find_the_highest_altitude(self, gain, expected):
        assert self.find_the_highest_altitude(gain) == expected
