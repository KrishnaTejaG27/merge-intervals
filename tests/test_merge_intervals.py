import pytest
from merge_intervals import merge_intervals

def test_example1():
    assert merge_intervals([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]

def test_touching_intervals():
    assert merge_intervals([[1,4],[4,5]]) == [[1,5]]

def test_empty():
    assert merge_intervals([]) == []

def test_single():
    assert merge_intervals([[1,4]]) == [[1,4]]

def test_unsorted_input():
    assert merge_intervals([[5,6],[1,3],[2,4]]) == [[1,4],[5,6]]

def test_contained_interval():
    assert merge_intervals([[1,10],[2,3],[4,5],[11,12]]) == [[1,10],[11,12]]
