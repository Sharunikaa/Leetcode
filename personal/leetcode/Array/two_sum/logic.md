# Two Sum - LeetCode Problem

## Problem Statement
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers that add up to the target. You may assume each input has exactly one solution, and you cannot use the same element twice.

**Example:**
- Input: `nums = [2, 7, 11, 15]`, `target = 9`
- Output: `[0, 1]`
- Explanation: `nums[0] + nums[1] = 2 + 7 = 9`

---

## Approach 1: Brute Force (Naive)

### Step-by-Step Working

1. **Use two nested loops** to check every pair of elements
2. **Outer loop:** Start from index `i = 0` to `len(nums) - 2`
3. **Inner loop:** Start from index `j = i + 1` to `len(nums) - 1`
4. **For each pair:** Check if `nums[i] + nums[j] == target`
5. **If match found:** Return `[i, j]` immediately
6. **Continue** until a pair is found

### Example Walkthrough
```
nums = [2, 7, 11, 15], target = 9

i=0, j=1: 2 + 7 = 9 ✓
Return [0, 1]
```

### Complexity Analysis - Brute Force

**Time Complexity: O(n²)**
- Outer loop runs n times
- Inner loop runs up to n times
- Total: n × n = **O(n²)** iterations

**Space Complexity: O(1)**
- No extra data structures used
- Only using indices for iteration

---

## Approach 2: Hash Map (Dictionary) - OPTIMAL

### Step-by-Step Working

1. **Initialize an empty dictionary** `d = {}` to store previously seen numbers as keys and their indices as values.

2. **Iterate through the array** with both index `i` and value `j`:
   - For each number, calculate the complement: `target - j`
   - Check if this complement already exists in the dictionary
   - If it does, we found our pair! Return `[index_of_complement, current_index]`
   - If not, add the current number and its index to the dictionary

3. **Continue until a pair is found** (guaranteed by problem constraints)

### Example Walkthrough
```
nums = [2, 7, 11, 15], target = 9

Iteration 1: i=0, j=2
  - complement = 9 - 2 = 7
  - 7 not in d
  - d = {2: 0}

Iteration 2: i=1, j=7
  - complement = 9 - 7 = 2
  - 2 is in d! d[2] = 0
  - Return [0, 1] ✓
```

---

## Logic Explanation

The key insight is using a **hash map to eliminate the nested loop**:

- **Naive approach:** Check every pair (brute force) - O(n²)
- **Optimized approach:** Store seen numbers in a hash map
  - When we see a number, we instantly check if its complement was already seen
  - If yes, we've found the answer
  - If no, we store it for future lookups

This transforms a two-pointer/brute force problem into a single-pass solution.

---

## Complexity Analysis

### Time Complexity: **O(n)**
- Single pass through the array
- Dictionary lookup and insertion: O(1) average case
- Total: `n` iterations × O(1) per iteration = **O(n)**

### Space Complexity: **O(n)**
- Dictionary can store up to `n` elements in worst case
- Storage: **O(n)** where n is the size of input array

---

## Comparison of Both Approaches

| Aspect | Brute Force | Hash Map |
|--------|------------|----------|
| **Time** | O(n²) | O(n) |
| **Space** | O(1) | O(n) |
| **Easy to understand?** | ✓ Yes | Moderate |
| **Efficient?** | ✗ No | ✓ Yes |
| **Best for** | Small arrays | Any size array |

**Recommendation:** Use **Hash Map approach** for interviews and production code due to superior time complexity.