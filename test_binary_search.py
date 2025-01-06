import pytest
from binary_search import binary_search

@pytest.mark.parametrize("cards, query, position",[
    ([24, 16, 13, 11, 9, 8, 5, 2], 2, 7),
    ([24, 17, 10, 11, 9, 8, 4], 24, 0),
    ([2], 2, 0),
    ([], 2, -1),
    ([20, 18, 17, 15, 8, 4, 2, 1, 0], 8, 4),
    ([9, 8, 8, 6, 5, 4, 2, 0], 8, 1),
    ([20, 20, 18, 18, 14, 14, 14, 12, 10, 9, 8, 5], 14, 4),
    ([20, 18, 15, 14, 13, 12, 1], 0, -1),
    ([-1, -2, -4, -6, -7, -9, -10, -12, -15, -20], -7, 4),
    ([10, 8, 7, 6, 4, 3, 1, 0, -1, -2, -4, -5, -6], -6, 12)
])
def test_linear_search(cards, query, position):
    assert binary_search(cards, query) == position