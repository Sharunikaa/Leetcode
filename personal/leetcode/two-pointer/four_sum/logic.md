# Four Sum Problem

## Problem Statement
Given an array of integers `nums` and an integer `target`, find all unique quadruplets (four numbers) in the array that add up to the target.

## Approach: Two Pointer with Nested Loops

### Algorithm
1. **Sort the array**: Start by sorting the array to enable two-pointer technique and easily skip duplicates
2. **First loop (i)**: Iterate through the array, fixing the first number
   - Skip duplicate values to avoid duplicate quadruplets
3. **Second loop (j)**: For each i, iterate to fix the second number
   - Skip duplicates to avoid duplicate quadruplets
4. **Two pointers (l, r)**: Use left and right pointers to find the remaining two numbers
   - Left pointer starts at `j+1`
   - Right pointer starts at `len(nums)-1`
   - Move pointers based on the sum:
     - If sum equals target: add to result, move both pointers, skip duplicates
     - If sum > target: move right pointer left (decrease sum)
     - If sum < target: move left pointer right (increase sum)

### Key Points
- **Sorting**: Enables two-pointer technique and duplicate skipping
- **Duplicate handling**: Skip when `nums[i]==nums[i-1]` and `nums[j]==nums[j-1]` to avoid duplicate results
- **Early termination**: The inner loop condition `i<len(nums)-3` ensures we have at least 4 elements

### Complexity Analysis
- **Time Complexity**: O(n³)
  - Outer loop: O(n)
  - Inner loop: O(n)
  - Two pointers: O(n)
  - Sorting: O(n log n)
- **Space Complexity**: O(1) excluding the output array (only using pointers)

### Example
```
nums = [1, 0, -1, 0, -2, 2]
target = 0

After sorting: [-2, -1, 0, 0, 1, 2]

Quadruplets that sum to 0:
[-2, -1, 1, 2]
[-2, 0, 0, 2]
[-1, 0, 0, 1]
```
