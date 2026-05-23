from modules.timsort import binary_search, insertion_sort, merge_arrs, merge_blocks, timsort

def test_binary_search():
    assert binary_search([5,4,3,2,1], 3) == 3
    assert binary_search([5,4,3,2,1], 6) == 0
    assert binary_search([-5, -4, 3, 3, -2, -1], -3) == 4
    assert binary_search([30, 20, -10], 15) == 2


def test_insertion_sort():
    arr = [1, 2, 3, 5, 2, 3, 4, 1]
    assert insertion_sort(arr, ordered_end=3, ascending=True) == sorted(arr)[::-1]
    assert insertion_sort([1, 2, 3, 1, 2, 3], ascending=False) == [3, 3, 2, 2, 1, 1]
    assert insertion_sort([5, 3, 2, 4, 1], ascending=False, ordered_end=4) == [5, 3, 2, 4, 1]


def test_merge_arrs():
    assert merge_arrs([5, 3, 1], [6, 4, 2]) == [6, 5, 4, 3, 2, 1]
    assert merge_arrs([3, 2, 1], [6, 5, 4]) == [6, 5, 4, 3, 2, 1]
    assert merge_arrs([], [3, 2, 1]) == [3, 2, 1]


def test_merge_blocks():
    assert merge_blocks([[2, 1], [4, 3]]) == [4, 3, 2 ,1]
    assert merge_blocks([[1], [2], [3]]) == [3, 2, 1]
    assert merge_blocks([[5, 1], [6, 2], [7, 3]]) == [7, 6, 5, 3, 2, 1]


def test_timsort():
    arrs = []
    arrs.append([int(x) for x in range(1000)])
    arrs.append([1])
    arrs.append([])
    arrs.append([3, 2, 1, 3, 2, 3, 1])
    for arr in arrs:
        assert timsort(arr) == sorted(arr)[::-1]
