# Valid Anagram - LeetCode Problem

## Problem Statement
Given two strings `s` and `t`, return `True` if `t` is an anagram of `s`, and `False` otherwise.

An **anagram** is a word formed by rearranging the letters of another word, using all original letters exactly once.

**Example:**
- Input: `s = "anagram"`, `t = "nagaram"`
- Output: `True`
- Explanation: Both strings contain the same characters with the same frequency

**Example:**
- Input: `s = "rat"`, `t = "car"`
- Output: `False`
- Explanation: 'r' appears in both, but 'a' and 't' are not in "car"

---

## Approach 1: Character Frequency Counting (ASCII Array)

### Step-by-Step Working

1. **Check length:** If `len(s) != len(t)`, they cannot be anagrams, return `False`

2. **Create frequency array:** Initialize array `f` of size 26 (for a-z) with all zeros

3. **Count characters in `s`:** For each character in `s`:
   - Get its ASCII value
   - Calculate index: `ord(char) - ord('a')` (converts a→0, b→1, ..., z→25)
   - Increment the frequency count at that index

4. **Subtract characters in `t`:** For each character in `t`:
   - Get its ASCII value
   - Calculate index: `ord(char) - ord('a')`
   - Decrement the frequency count at that index

5. **Verify all counts are zero:** If any frequency is non-zero, return `False`. Otherwise, return `True`

### Example Walkthrough
```
s = "anagram", t = "nagaram"

Step 1: len(s) = 7, len(t) = 7 ✓ Same length

Step 2: f = [0]*26

Step 3: Count s = "anagram"
  a: f[0] = 3
  n: f[13] = 1
  g: f[6] = 1
  r: f[17] = 1
  m: f[12] = 1

Step 4: Subtract t = "nagaram"
  n: f[13] = 0
  a: f[0] = 2
  g: f[6] = 0
  a: f[0] = 1
  r: f[17] = 0
  a: f[0] = 0
  m: f[12] = 0

Step 5: All frequencies = 0 ✓
Return True
```

### Complexity Analysis - ASCII Array

**Time Complexity: O(n)**
- First check: O(1)
- Count `s`: O(n) where n = len(s)
- Subtract `t`: O(n) where n = len(t)
- Verify array: O(26) = O(1)
- Total: **O(n)**

**Space Complexity: O(1)**
- Fixed-size array of 26 elements (for a-z)
- Space is constant regardless of input size: **O(1)**

---

## Approach 2: Sorting

### Step-by-Step Working

1. **Sort both strings:** Convert both `s` and `t` into sorted character lists

2. **Compare sorted strings:** Check if sorted `s` equals sorted `t`

3. **Return result:** If they're equal, they're anagrams

### Example Walkthrough
```
s = "anagram", t = "nagaram"

Step 1: Sort both
  sorted(s) = ['a', 'a', 'a', 'g', 'm', 'n', 'r']
  sorted(t) = ['a', 'a', 'a', 'g', 'm', 'n', 'r']

Step 2: Compare
  ['a', 'a', 'a', 'g', 'm', 'n', 'r'] == ['a', 'a', 'a', 'g', 'm', 'n', 'r'] ✓

Return True
```

### Complexity Analysis - Sorting

**Time Complexity: O(n log n)**
- Sorting `s`: O(n log n)
- Sorting `t`: O(n log n)
- Comparison: O(n)
- Total: **O(n log n)** (dominated by sorting)

**Space Complexity: O(n)**
- Sorted strings require O(n) space each
- Total: **O(n)** for storing sorted characters

---

## Comparison of Both Approaches

| Aspect | ASCII Array | Sorting |
|--------|------------|---------|
| **Time** | O(n) | O(n log n) |
| **Space** | O(1) | O(n) |
| **Easy to understand?** | Moderate | ✓ Yes |
| **Efficient?** | ✓ Yes | Less efficient |
| **Best for** | Production code | Quick implementation |

**Recommendation:** Use **ASCII Array approach** for better time complexity. The Sorting approach is simpler to code but slower for large inputs.

---

## Key Insights

1. **Anagrams must have:**
   - Same length
   - Same characters
   - Same character frequencies

2. **ASCII Array is optimal:**
   - Time: O(n) is better than O(n log n)
   - Space: O(1) is better than O(n)
   - No extra sorting overhead

3. **Why it works:**
   - If frequencies match after increment/decrement, all characters align perfectly
   - A mismatch in any frequency means different character composition
