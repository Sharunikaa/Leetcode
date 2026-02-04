# Rotate Array

## Problem
Rotate an array to the right by k steps.

Example: `[1,2,3,4,5]` with k=2 becomes `[4,5,1,2,3]`

## Approach: Pop and Insert

### Algorithm
1. Normalize k: If k > len(nums), take k % len(nums) to avoid unnecessary rotations
2. For each of k rotations:
   - Pop the last element from the array
   - Insert it at the beginning (index 0)

### Time Complexity
- **O(n*k)** where n is the length of the array
  - Each pop() and insert(0) operation is O(n)
  - We repeat this k times

### Space Complexity
- **O(1)** - Only modifying the array in-place

### Explanation
- The pop() removes the last element efficiently
- The insert(0) adds it at the front
- We repeat this k times to rotate the array to the right

### Trade-offs
**Pros:**
- Simple to understand and implement
- Modifies array in-place

**Cons:**
- Not the most efficient approach for large arrays
- Pop and insert operations are O(n) each
- Better approaches exist using reversal (O(n) time, O(1) space)
