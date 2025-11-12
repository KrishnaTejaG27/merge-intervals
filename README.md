# merge-intervals

Merge overlapping intervals.

## Problem
Given a list of intervals `[start, end]`, merge all overlapping intervals and return a list of the merged, disjoint intervals sorted by start time.

## Solution
Sort intervals by start and scan once to merge overlapping ranges. This yields an O(n log n) time solution due to the sort.

Run tests:
python -m venv .venv
source .venv/bin/activate
pip install -U pip pytest
pytest -q
