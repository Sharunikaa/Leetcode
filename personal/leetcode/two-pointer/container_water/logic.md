# Container With Most Water

## Problem
Given an array `h` of non-negative integers representing heights, find two lines that form a container to hold the maximum amount of water.

The area is calculated as: `width × min(height[left], height[right])`

Example: `[1,8,6,2,5,4,8,3,7]` should return `49` (between indices 1 and 8: width=7, height=8)

## Approach: Two-Pointer

### Algorithm
1. Initialize two pointers: `l` at the start and `r` at the end
2. Calculate the area formed by the two pointers
3. Track the maximum area found
4. Move the pointer pointing to the shorter line inward (because moving the taller line can only decrease area)
5. Repeat until pointers meet

### Key Insight
- The area is limited by the shorter line
- Moving the taller line inward can only decrease or maintain the area (width decreases, height won't increase beyond the shorter line)
- Moving the shorter line inward has a chance to increase the area (might find a taller line)

### Time Complexity
- **O(n)** - Single pass with two pointers

### Space Complexity
- **O(1)** - Only using a few variables

### Explanation
- Start with the widest container (full width)
- Calculate current area: `width × min(left_height, right_height)`
- Move the pointer with the smaller height inward
- Continue until pointers converge
- This greedy approach guarantees we explore all potentially better containers

### Example Trace
```
Input: [1,8,6,2,5,4,8,3,7]
       0 1 2 3 4 5 6 7 8

Start: l=0(h=1), r=8(h=7) → area = 8×1 = 8
Step1: l=1(h=8), r=8(h=7) → area = 7×7 = 49 ✓ (maximum)
Step2: l=1(h=8), r=7(h=3) → area = 6×3 = 18
... continue until l >= r
```

Result: **49**
