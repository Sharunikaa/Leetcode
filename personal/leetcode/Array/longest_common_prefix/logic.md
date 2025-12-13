# Longest Common Prefix - LeetCode Problem

## Problem Statement
Given an array of strings `strs`, return the longest common prefix string amongst all the strings in the array. If there is no common prefix, return an empty string `""`.

A **common prefix** is a string that appears as a prefix in all strings in the array.

**Example:**
- Input: `strs = ["flower","flow","flight"]`
- Output: `"fl"`
- Explanation: All strings start with "fl"

**Example:**
- Input: `strs = ["dog","racecar","car"]`
- Output: `""`
- Explanation: No common prefix exists

---

## Approach 1: Horizontal Scanning (Brute Force)

### Step-by-Step Working

1. **Initialize empty result:** `res = ""`

2. **Iterate through character positions** of the first string (0 to len(strs[0])-1)

3. **For each position i:**
   - Check all strings in the array
   - If any string is shorter than position i, or character at position i differs from first string, return current result
   - Otherwise, add the character to result

4. **Return the accumulated prefix**

### Example Walkthrough
```
strs = ["flower", "flow", "flight"]

i=0 (char='f'):
  - flower[0]='f', flow[0]='f', flight[0]='f' ✓
  - res = "f"

i=1 (char='l'):
  - flower[1]='l', flow[1]='l', flight[1]='l' ✓
  - res = "fl"

i=2 (char='o'):
  - flower[2]='o', flow[2]='o', flight[2]='i' ✗
  - Return "fl"
```

### Complexity Analysis - Brute Force

**Time Complexity: O(S)** where S = sum of all characters
- In worst case, we scan all characters of all strings
- S = length of first string × number of strings

**Space Complexity: O(1)**
- Only storing the result string (not counted as extra space)

---

## Approach 2: Sorted Comparison (Pointer-based)

### Step-by-Step Working

1. **Sort the strings array:** Sorts lexicographically
   - After sorting, only need to compare first and last strings
   - If first and last match at each position, middle strings definitely match

2. **Find minimum length:** Get the length of shortest string (avoid index out of bounds)

3. **Compare first and last strings:**
   - For each position j (0 to min_length)
   - If characters match, add to result
   - If they don't match, break

4. **Return the result**

### Why It Works
When array is sorted lexicographically:
- First string is smallest
- Last string is largest
- All other strings fall between them
- If extremes match at position j, all middle strings also match

### Example Walkthrough
```
strs = ["flower", "flow", "flight"]
After sort: ["flight", "flow", "flower"]

min_length = 4 (length of "flow")
first = "flight"
last = "flower"

j=0: 'f' == 'f' ✓ → r = "f"
j=1: 'l' == 'l' ✓ → r = "fl"
j=2: 'i' != 'o' ✗ → break

Return "fl"
```

### Complexity Analysis - Sorted Comparison

**Time Complexity: O(n log n + m)**
- Sorting: O(n log n) where n = number of strings
- Comparison: O(m) where m = length of shortest string
- Total: **O(n log n + m)** (sorting dominates)

**Space Complexity: O(1)**
- Only a few variables, no extra data structures

---

## Approach 3: Backward Prefix Matching (startswith)

### Step-by-Step Working

1. **Handle edge case:** If array is empty, return `""`

2. **Start with candidate:** Initialize prefix as the shortest string
   - `prefix = min(strs, key=len)` finds shortest string

3. **Shrink from right:**
   - While prefix is not empty:
   - Check if ALL strings start with current prefix using `startswith()`
   - If yes, return prefix (we found the answer!)
   - If no, remove last character: `prefix = prefix[:-1]`

4. **Continue until prefix is found or empty string returned**

### Example Walkthrough
```
strs = ["flower", "flow", "flight"]

Candidate prefix = "flow" (shortest string)

Iteration 1: "flow"
  - flower.startswith("flow")? ✓
  - flow.startswith("flow")? ✓
  - flight.startswith("flow")? ✗
  - Remove last char: "flo"

Iteration 2: "flo"
  - flower.startswith("flo")? ✓
  - flow.startswith("flo")? ✓
  - flight.startswith("flo")? ✗
  - Remove last char: "fl"

Iteration 3: "fl"
  - flower.startswith("fl")? ✓
  - flow.startswith("fl")? ✓
  - flight.startswith("fl")? ✓
  - Return "fl"
```

### Why It Works
- Start from the shortest string (guaranteed max prefix length)
- Systematically reduce prefix length until all strings match
- Early termination when common prefix found

### Complexity Analysis - startswith

**Time Complexity: O(n × m²)**
- m = length of shortest string
- For each iteration (m iterations): check all n strings
- Each `startswith()` check: O(m) in worst case
- Total: **O(n × m²)**

**Space Complexity: O(m)**
- Storing different prefix lengths during iterations

---

## Comparison of All Approaches

| Aspect | Brute Force | Sorted | startswith |
|--------|------------|--------|-----------|
| **Time** | O(S) | O(n log n + m) | O(n × m²) |
| **Space** | O(1) | O(1) | O(m) |
| **Easy to understand?** | ✓ Yes | Moderate | ✓ Yes |
| **Best case** | Very fast | Slow (sorts) | Moderate |
| **Worst case** | Slow | Slow (sorts) | Very slow |
| **Best for** | Production | Clever interviews | Simple code |

Where:
- `n` = number of strings
- `m` = length of shortest string
- `S` = total characters in all strings

**Recommendation:** Use **Brute Force approach** for best real-world performance.

---

## Key Insights

1. **Brute Force is optimal:**
   - O(S) is linear in total input size
   - Can't do better than reading all characters
   - Clean and straightforward implementation

2. **Sorting trick is clever but slower:**
   - Sorting overhead: O(n log n)
   - Only useful if demonstrating algorithmic creativity

3. **startswith is intuitive but inefficient:**
   - Repeated `startswith()` calls create redundant comparisons
   - O(n × m²) quickly becomes expensive

4. **All approaches handle edge cases:**
   - Empty arrays
   - Single string
   - No common prefix
   - Empty strings in array
