"""
merge_intervals.py

Given a list of intervals represented as pairs [start, end],
merge all overlapping intervals and return the result sorted by start.
"""
from typing import List

def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = []
    current_start, current_end = intervals[0]

    for s, e in intervals[1:]:
        if s <= current_end:
            current_end = max(current_end, e)
        else:
            merged.append([current_start, current_end])
            current_start, current_end = s, e

    merged.append([current_start, current_end])
    return merged

if __name__ == "__main__":
    examples = [
        [[1,3],[2,6],[8,10],[15,18]],
        [[1,4],[4,5]],
        [],
        [[1,4]]
    ]
    for ex in examples:
        print(ex, "->", merge_intervals(ex))
