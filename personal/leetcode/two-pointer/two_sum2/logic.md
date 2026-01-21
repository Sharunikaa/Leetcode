# Two Sum II - Input Array Is Sorted

## Problem
Given a 1-indexed array of integers that is **already sorted in non-decreasing order**, find two numbers such that they add up to a specific target number.

## Approaches

### 1. Two Pointer (Optimal - O(n) time, O(1) space)
- Use two pointers: left at start, right at end
- If sum equals target, return indices
- If sum is less than target, move left pointer right (increase sum)
- If sum is greater than target, move right pointer left (decrease sum)
- **Best for sorted arrays**

### 2. Hash Map / Dictionary (O(n) time, O(n) space)
- Iterate through array and store complements in dictionary
- For each number, check if its complement exists in dictionary
- If complement exists, return indices
- If not, add current number to dictionary

## Key Insight
Since the array is **sorted**, the two-pointer approach is preferred as it requires only constant extra space, unlike the hash map approach.
